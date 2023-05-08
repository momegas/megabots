import os
from megabots.bots.model import AddText, Index, SupportedEmbeddings
from megabots.bots.utils import _custom_openapi
from fastapi import FastAPI
from langchain.vectorstores.pgvector import PGVector
from langchain.embeddings.openai import OpenAIEmbeddings
from sqlmodel import Field, Session, SQLModel, create_engine, select
from langchain.vectorstores import Qdrant


cur_dir = os.path.dirname(os.path.abspath(__file__))
index_dir = os.path.join(cur_dir, "..", "examples", "files")

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
qdrant_url = "http://localhost:6333"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/v1/index")
async def create_index(index: Index):
    with Session(engine) as session:
        session.add(index)
        session.commit()
        session.refresh(index)
        return index


@app.get("/v1/indexes/")
def get_indexes():
    with Session(engine) as session:
        indexes = session.exec(select(Index)).all()
        return indexes


@app.post("/v1/index/{index_id}/add_text")
async def add_text(index_id: int, addText: AddText):
    with Session(engine) as session:
        index = session.get(Index, index_id)

        if not index:
            return {"error": "Index not found."}

        embeddings = None
        if index.embeddings == SupportedEmbeddings.OPEN_AI:
            embeddings = OpenAIEmbeddings()
        else:
            return {"error": "Embeddings not supported."}

        vector_db = Qdrant.from_texts(
            addText.texts,
            embeddings,
            url=qdrant_url,
            collection_name=index.name,
        )

        return


@app.post("/v1/bot")
async def create_bot():
    pass


@app.get(
    "/v1/bot/{bot_id}/ask/{question}",
    summary="Ask bot",
    description="Send question to the bot.",
    responses={200: {"description": "Bot answer"}},
)
async def ask(question: str):
    pass


app.openapi_schema = _custom_openapi(app, "0.0.0")
