from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory


class ConversationBuffer:
    def __init__(self):
        self.memory = ConversationBufferMemory(input_key="question")


class ConversationBufferWindow:
    def __init__(self, k: int):
        self.k: int = k
        self.memory = ConversationBufferWindowMemory(k=self.k, input_key="question")


SUPPORTED_MEMORY = {
    "conversation-buffer": {
        "impl": ConversationBuffer,
        "default": {},
    },
    "conversation-buffer-window": {
        "impl": ConversationBufferWindow,
        "default": {"k": 3},
    },
}


Memory = type("Memory", (ConversationBuffer, ConversationBufferWindow), {})


def memory(
    name: str = "conversation-buffer-window",
    k: int | None = None,
) -> Memory:
    if name is None:
        raise RuntimeError("Impossible to instantiate memory without a name.")

    if name not in SUPPORTED_MEMORY:
        raise ValueError(f"Memory {name} is not supported.")

    cl = SUPPORTED_MEMORY[name]["impl"]

    if name == "conversation-buffer-window":
        return cl(k=k)

    return SUPPORTED_MEMORY[name]["impl"]()
