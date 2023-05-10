from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select


class SupportedEmbeddings(str, Enum):
    OPEN_AI = "openai"


class Index(BaseModel):
    name: str
    size: int = 100


class AddText(BaseModel):
    texts: List[str]


class BotAnswerOutput(BaseModel):
    text: str


class SupportedModel(str, Enum):
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    TEXT_DAVINCI_003 = "text-davinci-003"


class SupportedMemory(str, Enum):
    CONVERSATION_BUFFER = "conversation-buffer"
    CONVERSATION_BUFFER_WINDOW = "conversation-buffer-window"


class Bot(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    llm: SupportedModel
    prompt: str
    memory: SupportedMemory
    index: str
