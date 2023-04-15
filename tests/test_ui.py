import gradio as gr
from megabots import create_interface


def test_create_interface():
    # create a mock Bot object
    class MockBot:
        def ask(self, question: str):
            return "Answer"

    # create a mock example
    example = [["What is your name?"], ["My name is Bot."]]

    # call the function with the mock bot and example
    interface = create_interface(MockBot(), examples=example)

    # check if the interface has the correct properties
    assert isinstance(interface, gr.Interface)
    assert len(interface.examples) == 2
    assert interface.examples == example
