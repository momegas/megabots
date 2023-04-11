# QnA Bot

Create a question answering over docs bot with one line of code:

```python
from qnabot import QnABot
import os

os.environ["OPENAI_API_KEY"] = "my key"

bot = QnABot(directory="./mydata")
```

### Here's how it works

High level overview what is happening under the hood:

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
