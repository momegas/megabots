from fastapi import FastAPI
from qnabot import QnABot


def create_app(bot: QnABot):
    app = FastAPI()

    @app.get("/v1/ask/{question}")
    async def ask(question: str):
        answer = bot.ask(question)
        return {"answer": answer}

    return app
