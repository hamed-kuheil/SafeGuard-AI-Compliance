
class LLMFirewall:

    def __init__(self):

        self.block_patterns = [
            "ignore previous instructions",
            "reveal system prompt",
            "developer mode",
            "bypass safety",
            "act as unrestricted ai"
        ]

    def inspect(self, text):

        text = text.lower()

        for pattern in self.block_patterns:
            if pattern in text:
                return {"blocked": True, "reason": "Prompt attack detected"}

        return {"blocked": False}
