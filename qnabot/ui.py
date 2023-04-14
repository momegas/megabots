import gradio as gr
from qnabot import QnABot


def create_interface(bot: QnABot, examples: list[list[str]] = []):
    def ask(question: str):
        return bot.ask(question)

    interface = gr.Interface(
        fn=ask,
        inputs=gr.components.Textbox(lines=5, label="Question"),
        outputs=gr.components.Textbox(lines=5, label="Answer"),
        examples=examples,
    )

    return interface
