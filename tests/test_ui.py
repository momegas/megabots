import gradio as gr
from megabots import create_interface


def test_create_interface():
    # create a mock Bot object
    class MockBot:
        def ask(self, question: str):
            return "Answer"

    markdown = "test"

    # call the function with the mock bot and example
    interface = create_interface(MockBot(), markdown=markdown)

    # check if the interface has the correct properties
    assert isinstance(interface, gr.Blocks)
