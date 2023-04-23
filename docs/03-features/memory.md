Adding memory to a bot makes the bot remember what you said in your conversation.
Lets see an example to better understand this:

```python
from megabots import bot

qnabot = bot("qna-over-docs", index="./index", memory="conversation-buffer")

print(qnabot.ask("who is iron man?"))
```

🤖: `Iron Man is a superhero character who is a member of the Avengers. He is known for his high-tech suit of armor and his alter ego, Tony Stark.`

The bot answers as expected. But what if you want to ask a follow up question?
Without memory you would have to specifically specify that you're talking about Iron Man.
But when the bot has memory you don't.

```python
print(qnabot.ask("was he in the first roster?"))
```

🤖: `Yes, Iron Man was part of the original Avengers lineup.`

Notice that the bot understands that we are talking about iron man.

### Memory types

In the example above we specified that the memory is of type `conversation-buffer`. There are more types and
you can even customize some of them. At the moment 🤖 Megabots supports the following memory types:

- `conversation-buffer`: the raw input of the past conversation between the human and AI is passed — in its raw form — to the `history` variable.
- `conversation-buffer-window`: acts in the same way as our earlier `conversation-buffer` but adds a window to the memory.
  Meaning that we only keep a given number of past interactions before “forgetting” them.

### Customizing memory

You can customize memory types by using the `memory` function.

```python
from megabots import bot, memory

qnabot = bot(
    "qna-over-docs",
    index="./index.pkl",
    memory=memory("conversation-buffer-window", k=5),
)

print(qnabot.ask("who is iron man?"))
print(qnabot.ask("was he in the first roster?"))
```

### Changing prompt when using memory

Assume you want to change the prompt while using memory with the bot. In the prompt below notice that a 3rd variable was added, `history`.
This is where the past conversations with the bot are injected so that the bot remembers what you said in the past.

```python
from megabots import bot

prompt = """
Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

{history}
Human: {question}
AI:"""

qnabot = bot(
    "qna-over-docs",
    prompt=prompt,
    index="./index.pkl",
    memory="conversation-buffer",
)

print(qnabot.ask("who is iron man?"))
print(qnabot.ask("was he in the first roster?"))
```
