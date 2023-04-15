import json
from fastapi.testclient import TestClient
from megabots import bot, create_api

qnabot = bot("qna-over-docs", index="./examples/files")
app = create_api(qnabot)

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
