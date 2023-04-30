import os
from megabots import bot
from megabots.utils import create_api

# from lcserve import serving

cur_dir = os.path.dirname(os.path.abspath(__file__))
index_dir = os.path.join(cur_dir, "..", "examples", "files")


mybot = bot("qna-over-docs", index="./index.pkl")


# @serving
# def ask(question: str) -> str:
#     return mybot.ask(question)


app = create_api(mybot)
