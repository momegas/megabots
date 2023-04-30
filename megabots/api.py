import os
from megabots import bot
from lcserve import serving

cur_dir = os.path.dirname(os.path.abspath(__file__))
index_dir = os.path.join(cur_dir, "..", "examples", "files")

print("hey")


@serving
def ask(question: str) -> str:
    mybot = bot("qna-over-docs", index=index_dir)
    return mybot.ask(question)
