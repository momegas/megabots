from typing import List
from langchain import PromptTemplate

QNA_TEMPLATE = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

{history}
Human: {question}
AI:"""

QA_MEMORY_PROMPT = PromptTemplate(
    template=QNA_TEMPLATE, input_variables=["context", "history", "question"]
)


def prompt(template: str, variables: List[str]):
    return PromptTemplate(template=template, input_variables=variables)
