import json
from fastapi.testclient import TestClient
from qnabot import QnABot, create_app

bot = QnABot(directory="./examples/files")
app = create_app(bot)

client = TestClient(app)


def test_successful_response():
    response = client.get("/v1/ask/What is your name?")
    assert response.status_code == 200
    assert "answer" in response.json()
    assert isinstance(response.json()["answer"], str)


def test_missing_question_parameter():
    response = client.get("/v1/ask/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
