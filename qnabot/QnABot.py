from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import DirectoryLoader, S3DirectoryLoader
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.vectorstores.faiss import FAISS
import pickle
import os
from langchain.chains.combine_documents.stuff import StuffDocumentsChain


class QnABot:
    def __init__(
        self,
        directory: str,
        index: str | None = None,
        model: str | None = None,
        verbose: bool = False,
        temperature: int = 0,
    ):
        # Initialize the QnABot by selecting a model, creating a loader,
        # and loading or creating an index
        self.select_model(model, temperature)
        self.create_loader(directory)
        self.load_or_create_index(index)

        # Load the question-answering chain for the selected model
        self.chain = load_qa_with_sources_chain(self.llm, verbose=verbose)

    def select_model(self, model: str | None, temperature: float):
        # Select and set the appropriate model based on the provided input
        if model is None or model == "gpt-3.5-turbo":
            print("Using model: gpt-3.5-turbo")
            self.llm = ChatOpenAI(temperature=temperature)

        if model == "text-davinci-003":
            print("Using model: text-davinci-003")
            self.llm = OpenAI(temperature=temperature)

    def create_loader(self, directory: str):
        # Create a loader based on the provided directory (either local or S3)
        if directory.startswith("s3://"):
            self.loader = S3DirectoryLoader(directory)
        else:
            self.loader = DirectoryLoader(directory, recursive=True)

    def load_or_create_index(self, index_path: str | None):
        # Load an existing index from disk or create a new one if not available
        if index_path is not None and os.path.exists(index_path):
            print("Loading path from disk...")
            with open(index_path, "rb") as f:
                self.search_index = pickle.load(f)
        else:
            print("Creating index...")
            self.search_index = FAISS.from_documents(
                self.loader.load_and_split(), OpenAIEmbeddings()
            )

    def save_index(self, index_path: str):
        # Save the index to the specified path
        with open(index_path, "wb") as f:
            pickle.dump(self.search_index, f)

    def print_answer(self, question: str, k=1):
        # Retrieve and print the answer to the given question
        input_documents = self.search_index.similarity_search(question, k=k)
        a = self.chain.run(input_documents=input_documents, question=question)
        print(a)

    def get_answer(self, question: str, k=1) -> str:
        # Retrieve the answer to the given question and return it
        input_documents = self.search_index.similarity_search(question, k=k)
        answer = self.chain.run(input_documents=input_documents, question=question)
        return answer
