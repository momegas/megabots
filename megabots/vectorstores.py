from typing import Type, TypeVar
from langchain.vectorstores import Milvus, Qdrant
from abc import ABC


class MilvusVectorStore:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.client = Milvus


SUPPORTED_VECTORSTORES = {
    "milvus": {
        "impl": MilvusVectorStore,
        "default": {"host": "localhost", "port": 19530},
    }
}


def vectorstore(name: str) -> MilvusVectorStore:
    """Return a vectorstore object."""

    if name is None:
        raise RuntimeError("Impossible to instantiate a vectorstore without a name.")

    if name not in SUPPORTED_VECTORSTORES:
        raise ValueError(f"Vectorstore {name} is not supported.")

    return SUPPORTED_VECTORSTORES[name]["impl"](
        host=SUPPORTED_VECTORSTORES[name]["default"]["host"],
        port=SUPPORTED_VECTORSTORES[name]["default"]["port"],
    )
