## Exposing an API with FastAPI

You can also create a FastAPI app that will expose the bot as an API using the create_app function.
Assuming you file is called `main.py` run `uvicorn main:app --reload` to run the API locally.
You should then be able to visit `http://localhost:8000/docs` to see the API documentation.

```python
from megabots import bot, create_api

app = create_app(bot("qna-over-docs"))
```