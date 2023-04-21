import pytest
from megabots.memory import (
    ConversationBufferWindow,
    ConversationSummaryBuffer,
    memory,
    Memory,
    SUPPORTED_MEMORY,
)


def test_memory_name_none():
    with pytest.raises(RuntimeError):
        memory(name=None)


def test_memory_not_supported():
    with pytest.raises(ValueError):
        memory(name="unsupported_memory_type")


def test_memory_conversation_buffer_window():
    mem_obj = memory(name="conversation-buffer-window", memory_window=5)
    assert isinstance(mem_obj, ConversationBufferWindow)
    assert mem_obj.memory_window == 5
    assert mem_obj.__class__ == SUPPORTED_MEMORY["conversation-buffer-window"]["impl"]


def test_memory_conversation_buffer_window_invalid_max_token_limit():
    with pytest.raises(ValueError):
        memory(name="conversation-buffer-window", memory_window=5, max_token_limit=10)


def test_memory_conversation_summary_buffer():
    mem_obj = memory(name="conversation-summary-buffer", max_token_limit=10)
    assert isinstance(mem_obj, ConversationSummaryBuffer)
    assert mem_obj.max_token_limit == 10
    assert mem_obj.__class__ == SUPPORTED_MEMORY["conversation-summary-buffer"]["impl"]


def test_memory_conversation_summary_buffer_invalid_memory_window():
    with pytest.raises(ValueError):
        memory(name="conversation-summary-buffer", memory_window=5, max_token_limit=10)
