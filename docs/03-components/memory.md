# Table of Contents

1. [Introduction](#introduction)
2. [Memory Management](#memory-management)
3. [Memory Persistence](#memory-persistence)
4. [Memory Usage Examples](#memory-usage-examples)
5. [Creating Custom Memory Modules](#creating-custom-memory-modules)

## Introduction
- [Overview of Memory](#overview-of-memory)
- [Role of Memory in ChatGPT](#role-of-memory-in-chatgpt)

## Memory Management
- [Memory Storage](#memory-storage)
- [Memory Retrieval](#memory-retrieval)
- [Memory Update and Deletion](#memory-update-and-deletion)

## Memory Persistence
- [Persistent Memory](#persistent-memory)
- [Session-Based Memory](#session-based-memory)

## Memory Usage Examples
- [Example 1: Remembering User Preferences](#example-1-remembering-user-preferences)
- [Example 2: Maintaining Conversation Context](#example-2-maintaining-conversation-context)
- [Example 3: Storing External Data](#example-3-storing-external-data)

## Creating Custom Memory Modules
- [Design Guidelines](#design-guidelines)
- [Implementation Steps](#implementation-steps)
- [Testing and Deployment](#testing-and-deployment)




## Working with memory

You can easily add memory to your `bot` using the `memory` parameter. It accepts a string with the type of the memory to be used. This defaults to some sane dafaults.
Should you need more configuration, you can use the `memory` function and pass the type of memory and the configuration you need.

```python
from megabots import bot

qnabot = bot("qna-over-docs", index="./index.pkl", memory="conversation-buffer")

print(qnabot.ask("who is iron man?"))
print(qnabot.ask("was he in the first roster?"))
# Bot should understand who "he" refers to.
```

Or using the `memory`factory function

```python
from megabots import bot, memory

mem("conversation-buffer-window", k=5)

qnabot = bot("qna-over-docs", index="./index.pkl", memory=mem)

print(qnabot.ask("who is iron man?"))
print(qnabot.ask("was he in the first roster?"))
```

NOTE: For the `qna-over-docs` bot, when using memory and passing your custom prompt, it is important to remember to pass one more variable to your custom prompt to facilitate for chat history. The variable name is `history`.

```python
from megabots import bot

prompt = """
Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

{history}
Human: {question}
AI:"""

qnabot = bot("qna-over-docs", prompt=prompt, index="./index.pkl", memory="conversation-buffer")

print(qnabot.ask("who is iron man?"))
print(qnabot.ask("was he in the first roster?"))
```