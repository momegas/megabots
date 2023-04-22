# Table of Contents

1. [Introduction](#introduction)
2. [Creating Vector Stores](#creating-vector-stores)
3. [Manipulating Vector Stores](#manipulating-vector-stores)
4. [Examples of Vector Store Usage](#examples-of-vector-store-usage)
5. [Creating Custom Vector Store Modules](#creating-custom-vector-store-modules)

## Introduction
- [Overview of Vector Stores](#overview-of-vector-stores)
- [Role of Vector Stores in ChatGPT](#role-of-vector-stores-in-chatgpt)

## Creating Vector Stores
- [Defining Vector Stores](#defining-vector-stores)
- [Initializing Vector Stores](#initializing-vector-stores)

## Manipulating Vector Stores
- [Adding and Updating Vectors](#adding-and-updating-vectors)
- [Querying Vectors](#querying-vectors)
- [Deleting Vectors](#deleting-vectors)

## Examples of Vector Store Usage
- [Example 1: Document Embedding Storage](#example-1-document-embedding-storage)
- [Example 2: Contextualized User Profiles](#example-2-contextualized-user-profiles)
- [Example 3: Knowledge Graph Representation](#example-3-knowledge-graph-representation)

## Creating Custom Vector Store Modules
- [Design Guidelines](#design-guidelines)
- [Implementation Steps](#implementation-steps)
- [Testing and Deployment](#testing-and-deployment)



## Using Megabots with Milvus (more DBs comming soon)

Megabots `bot` can also use Milvus as a backend for its search engine. You can find an example of how to do it below.

In order to run Milvus you need to follow [this guide](https://milvus.io/docs/example_code.md) to download a docker compose file and run it.
The command is:

```bash
wget https://raw.githubusercontent.com/milvus-io/pymilvus/v2.2.7/examples/hello_milvus.py
```

You can then [install Attu](https://milvus.io/docs/attu_install-docker.md) as a management tool for Milvus

```python
from megabots import bot

# Attach a vectorstore by passing the name of the database. Default port for milvus is 19530 and default host is localhost
# Point it to your files directory so that it can index the files and add them to the vectorstore
bot = bot("qna-over-docs", index="./examples/files/", vectorstore="milvus")

bot.ask("what was the first roster of the avengers?")
```

Or use the `vectorstore` factory function for more customisation

```python

from megabots import bot, vectorstore

milvus = vectorstore("milvus", host="localhost", port=19530)

bot = bot("qna-over-docs", index="./examples/files/", vectorstore=milvus)
```