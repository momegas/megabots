## Getting started

Note: This is a work in progress. The API might change.

### Installing Megabots

```bash
pip install megabots
```

### Placing the API_key to the system

To set the environment variables, you can use the following methods depending on your operating system:

1.  **For Unix-based systems (Linux and macOS):**
    
    In your terminal, you can export the environment variables like this:

```bash
    export OPENAI_API_KEY="your_api_key_here" 
```
Make sure to replace `your_api_key_here` with your actual API key.

Note that these variables will only be available in the current terminal session. To make them persistent, you can add the above `export` commands to your shell profile file (e.g., `~/.bashrc`, `~/.bash_profile`, or `~/.zshrc`).

1.  **For Windows:**
    
    You can set environment variables using the `setx` command in the Command Prompt:
```bash
    setx OPENAI_API_KEY "your_api_key_here" 
``` 

### Integrating your first bot

```python
from megabots import bot
import os

os.environ["OPENAI_API_KEY"] = "my key"

# Create a bot 👉 with one line of code. Automatically loads your data from ./index or index.pkl. 
# Keep in mind that you need to have one or another.
qnabot = bot("qna-over-docs")

# Ask a question
answer = bot.ask("How do I use this bot?")

# Save the index to save costs (GPT is used to create the index)
bot.save_index("index.pkl")

# Load the index from a previous run
qnabot = bot("qna-over-docs", index="./index.pkl")

# Or create the index from a directory of documents
qnabot = bot("qna-over-docs", index="./index")

# Change the model
qnabot = bot("qna-over-docs", model="text-davinci-003")
```


