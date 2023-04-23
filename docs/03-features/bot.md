## A simple bot

🤖 Megabots tries to make creating a bot as simple as one python command.
Let's create a simple bot that can answer questions over your documents.
Fist create a folder called `index` and place some `.txt` or `.pdf` files in it.
Then create a python file called `bot.py`.

Assume the files are about Avengers facts.

Your structure should look like this:

```bash
├── index
│   ├── file1.txt
│   └── file2.pdf
└── bot.py
```

No in `bot.py` add the following code:

```python
from megabots import bot

qnabot = bot("qna-over-docs")

qnabot.ask("what was the first roster of the avengers?")
```

🤖: `'The first roster of the Avengers included Iron Man, Thor, Hulk, Ant-Man, and the Wasp.'`

That's it! You now have a bot that can answer questions over your documents.

## Adding sources

You can make your bot return the sources it found the info from with simply by passing `sources=True`.
When `sources` is `True` the bot will also include sources in the response.

🚨 A known [issue](https://github.com/hwchase17/langchain/issues/2858) exists,
where if you pass a custom prompt with sources the code breaks.

```python
from megabots import bot

qnabot = bot("qna-over-docs", sources=True)

qnabot.ask("what was the first roster of the avengers?")
```

🤖: `'The first roster of the Avengers included Iron Man, Thor, Hulk, Ant-Man, and the Wasp.\nSOURCES: examples/files/facts.txt'`
