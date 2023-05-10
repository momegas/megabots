import os
from megabots.model import AddText, Bot, Index, SupportedEmbeddings
from megabots.bots.utils import _custom_openapi
from fastapi import FastAPI
from langchain.vectorstores.pgvector import PGVector
from langchain.embeddings.openai import OpenAIEmbeddings
from sqlmodel import Field, Session, SQLModel, create_engine, select
from langchain.vectorstores import Qdrant
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

cur_dir = os.path.dirname(os.path.abspath(__file__))
index_dir = os.path.join(cur_dir, "..", "examples", "files")

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

qdrant_url = "http://localhost:6333"
client = QdrantClient(url=qdrant_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/v1/index")
async def create_index(index: Index):
    res = client.create_collection(
        collection_name=index.name,
        vectors_config=VectorParams(size=index.size or 100, distance=Distance.COSINE),
    )

    return res


@app.get("/v1/indexes/")
def get_indexes():
    return client.get_collections()


@app.post("/v1/index/{index_name}/add_text")
async def add_text(index_name: str, addText: AddText):
    index = client.get_collection(index_name)

    if not index:
        return {"error": "Index not found."}

    embeddings = OpenAIEmbeddings()

    Qdrant.from_texts(
        addText.texts,
        embeddings,
        url=qdrant_url,
        collection_name=index_name,
    )

    return True


@app.get(
    "/v1/qna/{index_name}/ask/{question}",
    summary="Ask bot",
    description="Send question to the bot.",
    responses={200: {"description": "Bot answer"}},
)
async def ask(index_name: str, question: str):
    embeddings = OpenAIEmbeddings()

    client = QdrantClient(url=qdrant_url)
    qdrant = Qdrant(
        client=client,
        collection_name=index_name,
        embedding_function=embeddings.embed_query,
    )

    docs = qdrant.similarity_search(question, top_k=3)

    llm = ChatOpenAI(temperature=0)

    chain = load_qa_chain(llm, chain_type="stuff")
    result = chain.run(input_documents=docs, question=question)

    return result


app.openapi_schema = _custom_openapi(app, "0.0.0")
