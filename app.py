"""
This file is an example of what you can build with 🤖Megabots.
It is hosted here: https://huggingface.co/spaces/momegas/megabots

"""

from megabots import bot, create_interface

prompt = """
You are programming assistant that helps programmers develop apps with the Megabots library.
Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.
If the question asks for python code you can provide it.

Context:
{context}

Conversation history:
{history}
Human: {question}
AI:
"""

qnabot = bot(
    "qna-over-docs",
    index="./examples/files",
    memory="conversation-buffer-window",
    prompt=prompt,
)


text = """
You can ask this bot anything about 🤖Megabots. Here are some examples:
- What is Megabots?
- How can I create a bot?
- How can I change the prompt?
- How can I create a bot that has memory and can connect to a milvus vector database?
- How can I customise the bot function?
- How can I an API out of my bot?
- How can I an intrface out of my bot?
- Where can i find the megabots repo?
"""

iface = create_interface(qnabot, text)
iface.launch()
