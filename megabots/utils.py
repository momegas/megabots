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


def create_interface(bot_instance: Bot, markdown: str = ""):
    with gr.Blocks() as interface:
        gr.Markdown(markdown)
        chatbot = gr.Chatbot([], elem_id="chatbot").style(height=450)
        msg = gr.Textbox(
            show_label=False,
            placeholder="Enter text and press enter",
        ).style(container=False)

        def user(user_message, history):
            return "", history + [[user_message, None]]

        def bot(history):
            print("im here")
            response = bot_instance.ask(history[-1][0])
            history[-1][1] = response
            return history

        msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
            bot, chatbot, chatbot
        )

    return interface
