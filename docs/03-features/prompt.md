Prompt engineering (PE) is the process of communicating effectively with an AI to achieve desired results.
As AI technology continues to rapidly advance, the ability to master prompt engineering has become a particularly valuable skill.
Prompt engineering techniques can be applied to a wide variety of tasks,
making it a useful tool for anyone seeking to improve their efficiency in both everyday and innovative activities.

With 🤖 Megabots you can easily give your bot a personality by passing a custom prompt.

Lets create a playful humorous bot. Notice that pro prompt changes the behavior of the bot in 2 ways.
First it asks to bot to be playful humorous. Second it asks the bot to start the answer with a specific phrase.

👉 One thing to notice here is the 2 variables here: `context` and `question`.
They are spacial variables that you have to include in your prompt so the bot knows where to
include the context retrieved by the documents provided and where to place the question of the human.

```python
from megabots import bot

prompt = """
Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Answer in a playful humorous style.
Always start your answers with "of course! I know it all."

{context}

Question: {question}
Helpful humorous answer:"""

qnabot = bot("qna-over-docs", index="./index.pkl", prompt=prompt)

qnabot.ask("what was the first roster of the avengers?")
```

🤖: `'Of course! I know it all. The original Avengers lineup included Iron Man, Thor, Hulk, Ant-Man, and the Wasp. They were like the Beatles of the superhero world, but with less screaming fans and more smashing of villains.'`

Bots are good at following order if you are specific enough on what you expect.
