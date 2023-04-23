# 🤖 Megabots

[![Tests](https://github.com/momegas/qnabot/actions/workflows/python-package.yml/badge.svg)](https://github.com/momegas/qnabot/actions/workflows/python-package.yml)
[![Python Version](https://img.shields.io/badge/python-%203.10%20-blue.svg)](#supported-python-versions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/License-MIT-informational.svg)](https://github.com/momegas/megabots/blob/main/LICENCE)
![](https://dcbadge.vercel.app/api/server/zkqDWk5S7P?style=flat&n&compact=true)

🤖 Megabots provides State-of-the-art, production ready LLM apps made mega-easy, so you don't have to build them from scratch 🤯 Create a bot, now 🫵

- 👉 Join us on Discord: [https://discord.gg/zkqDWk5S7P](https://discord.gg/zkqDWk5S7P)
- ✈️ Work is managed in this project: [https://github.com/users/momegas/projects/5/views/2](https://github.com/users/momegas/projects/5/views/2)
- 🤖 Documentation bot: [https://huggingface.co/spaces/momegas/megabots](https://huggingface.co/spaces/momegas/megabots)

**Megabots can be used to easily create bots that:**

- ⌚️ are production ready, in minutes
- 🗂️ can answer questions over documents
- 💾 can connect to vector databases and have memory
- 🎖️ automatically expose the bot as a rebust API using FastAPI (early release)
- 🏓 automatically expose the bot as a UI using Gradio

**Coming soon:**

- 🗣️ accept voice as an input using [whisper](https://github.com/openai/whisper)
- 👍 validate and correct the outputs of LLMs using [guardrails](https://github.com/ShreyaR/guardrails)
- 💰 semanticly cache LLM Queries and reduce Costs by 10x using [GPTCache](https://github.com/zilliztech/GPTCache)
- 🏋️ mega-easy LLM training
- 🚀 mega-easy deployment

🤖 Megabots is backed by some of the most famous tools for productionalising AI. It uses [LangChain](https://docs.langchain.com/docs/) for managing LLM chains, [FastAPI](https://fastapi.tiangolo.com/) to create a production ready API, [Gradio](https://gradio.app/) to create a UI. At the moment it uses [OpenAI](https://openai.com/) to generate answers, but we plan to support other LLMs in the future.

Let's create a bot that can answer questions over your docs in one line of code:

```bash
pip install megabots
```

```python
from megabots import bot

# Automatically loads your data from ./index or index.pkl.
qnabot = bot("qna-over-docs")
```

That's it!

There is a lot more to 🤖 Megabots. Have a look around.
