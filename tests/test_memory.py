from pytest import raises
from megabots import memory
from megabots.memory import ConversationBuffer, ConversationBufferWindow


def test_memory_conversation_buffer():
    mem = memory(name="conversation-buffer")
    assert isinstance(mem, ConversationBuffer)


def test_memory_conversation_buffer_window():
    mem = memory(name="conversation-buffer-window", k=10)
    assert isinstance(mem, ConversationBufferWindow)


def test_memory_unsupported_name():
    with raises(ValueError, match=r"Memory invalid-name is not supported."):
        memory(name="invalid-name")


def test_memory_no_name():
    with raises(
        RuntimeError, match=r"Impossible to instantiate memory without a name."
    ):
        memory(name=None)
