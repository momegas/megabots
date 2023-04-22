import gradio as gr
from fastapi import FastAPI
from megabots.bot import Bot


def create_api(bot: Bot):
    app = FastAPI()

    @app.get("/v1/ask/{question}")
    async def ask(question: str):
        answer = bot.ask(question)
        return {"answer": answer}

    return app


def create_interface(bot_instance: Bot, examples: list[list[str]] = []):
    with gr.Blocks() as interface:
        chatbot = gr.Chatbot([], elem_id="chatbot").style(height=750)
        msg = gr.Textbox(
            show_label=False,
            placeholder="Enter text and press enter, or upload an image",
        ).style(container=False)
        clear = gr.Button("Clear")

        def user(user_message, history):
            return "", history + [[user_message, None]]

        def bot(history):
            response = bot_instance.ask(history[-1][0])
            history[-1][1] = response
            return history

        msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
            bot, chatbot, chatbot
        )
        clear.click(lambda: None, None, chatbot, queue=False)

    return interface
