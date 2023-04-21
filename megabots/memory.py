from langchain.memory import (
    ConversationBufferMemory,
    ConversationBufferWindowMemory,
    ConversationSummaryMemory,
    ConversationSummaryBufferMemory,
)


class ConversationBuffer:
    def __init__(self):
        self.memory = ConversationBufferMemory


class ConversationBufferWindow:
    def __init__(self, memory_window: int):
        self.memory_window: int = memory_window
        self.memory = ConversationBufferWindowMemory


class ConversationSummary:
    def __init__(self):
        self.memory = ConversationSummaryMemory


class ConversationSummaryBuffer:
    def __init__(self, max_token_limit: int):
        self.max_token_limit: int = max_token_limit
        self.memory = ConversationSummaryBufferMemory


SUPPORTED_MEMORY = {
    "conversation-buffer": {
        "impl": ConversationBuffer,
        "default": {},
    },
    "conversation-buffer-window": {
        "impl": ConversationBufferWindow,
        "default": {"memory_window": 3},
    },
    "conversation-summary": {
        "impl": ConversationSummary,
        "default": {},
    },
    "conversation-summary-buffer": {
        "impl": ConversationSummaryBuffer,
        "default": {"max_token_limit": 40},
    },
}


Memory = type(
    "Memory",
    (
        ConversationBuffer,
        ConversationBufferWindow,
        ConversationSummary,
        ConversationSummaryBuffer,
    ),
    {},
)


def memory(
    name: str = "conversation-buffer-window",
    memory_window: int | None = None,
    max_token_limit: int | None = None,
) -> Memory:
    if name is None:
        raise RuntimeError("Impossible to instantiate memory without a name.")

    if name not in SUPPORTED_MEMORY:
        raise ValueError(f"Memory {name} is not supported.")

    cl = SUPPORTED_MEMORY[name]["impl"]

    if name == "conversation-buffer-window":
        if max_token_limit != None:
            raise ValueError(f"max_token_limit cannot be set for {name} memory")
        return cl(memory_window=memory_window)

    if name == "conversation-summary-buffer":
        if max_token_limit != None:
            raise ValueError(f"memory_window cannot be set for {name} memory")
        return cl(max_token_limit=max_token_limit)

    return SUPPORTED_MEMORY[name]["impl"]()
