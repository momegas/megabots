from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import DirectoryLoader, S3DirectoryLoader
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.vectorstores.faiss import FAISS
import gradio as gr
from fastapi import FastAPI
import pickle
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.chains.conversational_retrieval.prompts import (
    CONDENSE_QUESTION_PROMPT,
    QA_PROMPT,
)

load_dotenv()


class Bot:
    def __init__(
        self,
        model: str | None = None,
        prompt_template: str | None = None,
        prompt_variables: list[str] | None = None,
        memory: str | None = None,
        index: str | None = None,
        sources: bool | None = False,
        verbose: bool = False,
        temperature: int = 0,
    ):
        self.select_model(model, temperature)
        self.create_loader(index)
        self.load_or_create_index(index)

        # Load the question-answering chain for the selected model
        self.chain = self.create_chain(
            prompt_template, prompt_variables, verbose=verbose
        )

    def create_chain(
        self,
        prompt_template: str | None = None,
        prompt_variables: list[str] | None = None,
        verbose: bool = False,
    ):
        prompt = (
            PromptTemplate(template=prompt_template, input_variables=prompt_variables)
            if prompt_template is not None and prompt_variables is not None
            else QA_PROMPT
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

    def load_or_create_index(self, index_path: str):
        # Load an existing index from disk or create a new one if not available

        # Is pickle
        if index_path is not None and "pkl" in index_path or "pickle" in index_path:
            print("Loading path from disk...")
            with open(index_path, "rb") as f:
                self.search_index = pickle.load(f)
            return

        # Is directory
        if index_path is not None and os.path.isdir(index_path):
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
            "prompt": "",
            "temperature": 0,
            "index": "./files",
        },
    }
}

SUPPORTED_MODELS = {}


def bot(
    task: str | None = None,
    model: str | None = None,
    prompt_template: str | None = None,
    prompt_variables: list[str] | None = None,
    index: str | None = None,
    verbose: bool = False,
    temperature: int = 0,
    **kwargs,
) -> Bot:
    """Instanciate a bot based on the provided task. Each supported tasks has it's own default sane defaults.

    Args:
        task (str | None, optional): The given task. Can be one of the SUPPORTED_TASKS.
        model (str | None, optional): Model to be used. Can be one of the SUPPORTED_MODELS.
        index (str | None, optional): Data that the model will load and store index info.
        Can be either a local file path, a pickle file, or a url of a vector database.
        By default it will look for a local directory called "files" in the current working directory.
        verbose (bool, optional): Verbocity. Defaults to False.

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
        **kwargs,
    )


def create_api(bot: Bot):
    app = FastAPI()

    @app.get("/v1/ask/{question}")
    async def ask(question: str):
        answer = bot.ask(question)
        return {"answer": answer}

    return app


def create_interface(bot: Bot, examples: list[list[str]] = []):
    def ask(question: str):
        return bot.ask(question)

    interface = gr.Interface(
        fn=ask,
        inputs=gr.components.Textbox(lines=5, label="Question"),
        outputs=gr.components.Textbox(lines=5, label="Answer"),
        examples=examples,
    )

    return interface
