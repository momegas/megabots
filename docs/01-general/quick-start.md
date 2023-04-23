### Installing Megabots

```bash
pip install megabots
```

### Your first bot

Create a bot with one line of code. Automatically loads your data from `./index` or `index.pkl`.
Keep in mind that you need to have one or another.

```python
from megabots import bot

qnabot = bot("qna-over-docs")

answer = bot.ask("How do I use this bot?")
```

## API Keys

Some LLM vendors like Hugging Face, OpenAI, Anthropic, etc require an API key. Let's see how to set them up with Open AI API key as an example.

### Using .env files

An .env file is a plain text file that contains key-value pairs of environment variables that are meant to be used by an application or a script usually at the root of the porject.
Megabots loads `.env` files automatically. An example `.env` file would look like this:

```bash
OPENAI_API_KEY="your_api_key_here"
```

### Environment variables

To set the environment variables, you can use the following methods depending on your operating system:

**For Unix-based systems (Linux and macOS):**

In your terminal, you can export the environment variables like this:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Make sure to replace `your_api_key_here` with your actual API key.

Note that these variables will only be available in the current terminal session.

**For Windows:**

You can set environment variables using the `setx` command in the Command Prompt:

```bash
setx OPENAI_API_KEY "your_api_key_here"
```
