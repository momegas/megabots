from setuptools import setup, find_packages

VERSION = "0.0.11"

setup(
    name="megabots",
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        "langchain",
        "tiktoken",
        "unstructured",
        "fastapi",
        "faiss-cpu",
        "pdfminer.six",
        "gradio",
        "python-dotenv",
        "openai",
    ],
    author="Megaklis Vasilakis",
    author_email="megaklis.vasilakis@gmail.com",
    description="🤖 Megabots provides State-of-the-art, production ready bots made mega-easy, so you don't have to build them from scratch 🤯 Create a bot, now 🫵",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/momegas/megabots",
    keywords = [
    "bot"
    "qna-bot"
    "information-retrieval",
    "chatbot",
    "question-answering",
    "prompt-engineering"
    ]
    license="MIT",
    classifiers=[
        # Choose appropriate classifiers from
        # https://pypi.org/classifiers/
        "Development Status :: 4 - Beta"
    ],
)
