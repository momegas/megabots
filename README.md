# QnA Bot

[![Tests](https://github.com/momegas/qnabot/actions/workflows/python-package.yml/badge.svg)](https://github.com/momegas/qnabot/actions/workflows/python-package.yml)

Create a question answering over docs bot with one line of code:

```bash
pip install qnabot
```

```python
from qnabot import QnABot
import os

os.environ["OPENAI_API_KEY"] = "my key"

# Create a bot 👉 with one line of code
bot = QnABot(directory="./mydata")

# Ask a question
answer = bot.ask("How do I use this bot?")

# Save the index to save costs (GPT is used to create the index)
bot.save_index("index.pickle")

# Load the index from a previous run
bot = QnABot(directory="./mydata", index="index.pickle")
```

### Features

- [x] Create a question answering bot over your documents with one line of code using GPT
- [x] Save / load index to reduce costs (Open AI embedings are used to create the index)
- [x] Local data source (directory of documents) or S3 data source
- [x] FAISS for storing vectors / index
- [ ] Support for other vector databases (e.g. Weaviate, Pinecone)
- [ ] Customise prompt
- [ ] Expose API
- [ ] Support for LLaMA model
- [ ] Support for Anthropic models
- [ ] CLI / UI

### Here's how it works

Large language models (LLMs) are powerful, but they can't answer questions about documents they haven't seen. If you want to use an LLM to answer questions about documents it was not trained on, you have to give it information about those documents. To solve this, we use "retrieval augmented generation."

In simple terms, when you have a question, you first search for relevant documents. Then, you give the documents and the question to the language model to generate an answer. To make this work, you need your documents in a searchable format (an index). This process involves two main steps: (1) preparing your documents for easy querying, and (2) using the retrieval augmented generation method.

`QnABot` uses FAISS to create an index of documents and GPT to generate answers.

```mermaid
sequenceDiagram
    actor User
    participant API
    participant LLM
    participant Vectorstore
    participant IngestionEngine
    participant DataLake
    autonumber

    Note over API, DataLake: Ingestion phase
    loop Every X time
    IngestionEngine ->> DataLake: Load documents
    DataLake -->> IngestionEngine: Return data
    IngestionEngine -->> IngestionEngine: Split documents and Create embeddings
    IngestionEngine ->> Vectorstore: Store documents and embeddings
    end

    Note over API, DataLake: Generation phase

    User ->> API: Receive user question
    API ->> Vectorstore: Lookup documents in the index relevant to the question
    API ->> API: Construct a prompt from the question and any relevant documents
    API ->> LLM: Pass the prompt to the model
    LLM -->> API: Get response from model
    API -->> User: Return response

```
