import os
import tempfile
from megabots import bot
import pickle
from langchain.vectorstores.faiss import FAISS


# Define test data
test_directory = "./examples/files"
test_question = "what was the first roster of avengers in comics?"
correct_answer = "Iron Man, Thor, Hulk, Ant-Man"
sources = "SOURCES:"


def test_ask():
    qnabot = bot("qna-over-docs", index=test_directory)
    answer = qnabot.ask(test_question)

    # Assert that the answer contains the correct answer
    assert correct_answer in answer
    # Assert that the answer contains the sources
    assert sources not in answer


def test_save_load_index():
    # Create a temporary directory and file path for the test index
    with tempfile.TemporaryDirectory() as temp_dir:
        index_path = os.path.join(temp_dir, "test_index.pkl")

        # Create a bot and save the index to the temporary file path
        qnabot = bot("qna-over-docs", index=test_directory)
        qnabot.save_index(index_path)

        # Load the saved index and assert that it is the same as the original index
        with open(index_path, "rb") as f:
            saved_index = pickle.load(f)
        assert isinstance(saved_index, FAISS)

        bot_with_predefined_index = bot("qna-over-docs", index=index_path)

        # Assert that the bot returns the correct answer to the test question
        assert correct_answer in bot_with_predefined_index.ask(test_question)
