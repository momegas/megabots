from typing import Any
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.vectorstores.faiss import FAISS
import pickle
import os
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.chains.conversational_retrieval.prompts import QA_PROMPT
from langchain.document_loaders import DirectoryLoader
from megabots.vectorstore import VectorStore
from megabots.memory import Memory
import megabots


class Bot:
    def __init__(
        self,
        model: str | None = None,
        prompt_template: str | None = None,
        prompt_variables: list[str] | None = None,
        index: str | None = None,
        sources: bool | None = False,
        vectorstore: VectorStore | None = None,
        memory: Memory | None = None,
        verbose: bool = False,
        temperature: int = 0,
    ):
        self.select_model(model, temperature)
        self.create_loader(index)
        self.load_or_create_index(index, vectorstore)
        self.vectorstore = vectorstore
        self.memory = memory
        # Load the question-answering chain for the selected model
        self.chain = self.create_chain(
            prompt_template, prompt_variables, sources=sources, verbose=verbose
        )

    def create_chain(
        self,
        prompt_template: str | None = None,
        prompt_variables: list[str] | None = None,
        sources: bool | None = False,
        verbose: bool = False,
    ):
        prompt = (
            PromptTemplate(template=prompt_template, input_variables=prompt_variables)
            if prompt_template is not None and prompt_variables is not None
            else QA_PROMPT
        )
        # TODO: Changing the prompt here is not working. Leave it as is for now.
        # Reference: https://github.com/hwchase17/langchain/issues/2858
        if sources:
            return load_qa_with_sources_chain(
                self.llm, chain_type="stuff", verbose=verbose
            )
        return load_qa_chain(
            self.llm, chain_type="stuff", verbose=verbose, prompt=prompt
        )

    def select_model(self, model: str | None, temperature: float):
        # Select and set the appropriate model based on the provided input
        if model is None or model == "gpt-3.5-turbo":
            print("Using model: gpt-3.5-turbo")
            self.llm = ChatOpenAI(temperature=temperature)

        if model == "text-davinci-003":
            print("Using model: text-davinci-003")
            self.llm = OpenAI(temperature=temperature)

    def create_loader(self, index: str | None):
        # Create a loader based on the provided directory (either local or S3)
        if index is None:
            raise RuntimeError(
                """
            Impossible to find a valid index. 
            Either provide a valid path to a pickle file or a directory.               
            """
            )
        self.loader = DirectoryLoader(index, recursive=True)

    def load_or_create_index(self, index: str, vectorstore: VectorStore | None = None):
        # Load an existing index from disk or create a new one if not available
        if vectorstore is not None:
            self.search_index = vectorstore.client.from_documents(
                self.loader.load_and_split(),
                OpenAIEmbeddings(),
                connection_args={"host": vectorstore.host, "port": vectorstore.port},
            )
            return

        # Is pickle
        if index is not None and "pkl" in index or "pickle" in index:
            print("Loading path from pickle file: ", index, "...")
            with open(index, "rb") as f:
                self.search_index = pickle.load(f)
            return

        # Is directory
        if index is not None and os.path.isdir(index):
            print("Creating index...")
            self.search_index = FAISS.from_documents(
                self.loader.load_and_split(), OpenAIEmbeddings()
            )
            return

        raise RuntimeError(
            """
            Impossible to find a valid index. 
            Either provide a valid path to a pickle file or a directory.               
            """
        )

    def save_index(self, index_path: str):
        # Save the index to the specified path
        with open(index_path, "wb") as f:
            pickle.dump(self.search_index, f)

    def ask(self, question: str, k=1) -> str:
        # Retrieve the answer to the given question and return it
        input_documents = self.search_index.similarity_search(question, k=k)
        answer = self.chain.run(input_documents=input_documents, question=question)
        return answer


SUPPORTED_TASKS = {
    "qna-over-docs": {
        "impl": Bot,
        "default": {
            "model": "gpt-3.5-turbo",
            "temperature": 0,
            "index": "./index",
        },
    }
}

SUPPORTED_MODELS = {}


def bot(
    task: str | None = None,
    model: str | None = None,
    index: str | None = None,
    prompt_template: str | None = None,
    prompt_variables: list[str] | None = None,
    memory: str | Memory | None = None,
    vectorstore: str | VectorStore | None = None,
    verbose: bool = False,
    temperature: int = 0,
) -> Bot:
    """Instanciate a bot based on the provided task. Each supported tasks has it's own default sane defaults.

    Args:
        task (str | None, optional): The given task. Can be one of the SUPPORTED_TASKS.
        model (str | None, optional): Model to be used. Can be one of the SUPPORTED_MODELS.
        index (str | None, optional): Data that the model will load and store index info.
        Can be either a local file path, a pickle file, or a url of a vector database.
        By default it will look for a local directory called "files" in the current working directory.
        prompt_template (str | None, optional): Prompt template to be used. Specify variables with {var_name}.
        prompt_variables (list[str] | None, optional): Prompt variables to be used in the prompt template.
        verbose (bool, optional): Verbocity. Defaults to False.
        temperature (int, optional): Temperature. Defaults to 0.

    Raises:
        RuntimeError: _description_
        ValueError: _description_

    Returns:
        Bot: Bot instance
    """

    if task is None:
        raise RuntimeError("Impossible to instantiate a bot without a task.")
    if task not in SUPPORTED_TASKS:
        raise ValueError(f"Task {task} is not supported.")

    task_defaults = SUPPORTED_TASKS[task]["default"]

    return SUPPORTED_TASKS[task]["impl"](
        model=model or task_defaults["model"],
        index=index or task_defaults["index"],
        prompt_template=prompt_template,
        prompt_variables=prompt_variables,
        temperature=temperature,
        verbose=verbose,
        vectorstore=megabots.vectorstore(vectorstore)
        if isinstance(vectorstore, str)
        else vectorstore,
        memory=megabots.memory(memory) if isinstance(memory, str) else memory,
    )
