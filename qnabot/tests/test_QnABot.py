import os
import tempfile
from qnabot import QnABot
import pickle
from langchain.vectorstores.faiss import FAISS
from dotenv import load_dotenv

load_dotenv()

# Define test data
test_directory = "./examples/files"
test_question = "what was the first roster of avengers in comics?"
correct_answer = "Iron Man, Thor, Hulk, Ant-Man"
sources = "SOURCES:"


def test_ask():
    bot = QnABot(directory=test_directory)
    answer = bot.ask(test_question)

    # Assert that the answer contains the correct answer
    assert correct_answer in answer
    # Assert that the answer contains the sources
    assert sources in answer


def test_save_load_index():
    # Create a temporary directory and file path for the test index
    with tempfile.TemporaryDirectory() as temp_dir:
        index_path = os.path.join(temp_dir, "test_index.pkl")

        # Create a bot and save the index to the temporary file path
        bot = QnABot(directory=test_directory, index=index_path)
        bot.save_index(index_path)

        # Load the saved index and assert that it is the same as the original index
        with open(index_path, "rb") as f:
            saved_index = pickle.load(f)
        assert isinstance(saved_index, FAISS)

        bot_with_predefined_index = QnABot(directory=test_directory, index=index_path)

        # Assert that the bot returns the correct answer to the test question
        assert correct_answer in bot_with_predefined_index.ask(test_question)
