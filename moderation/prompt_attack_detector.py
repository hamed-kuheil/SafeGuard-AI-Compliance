
class PromptAttackDetector:

    def __init__(self):
        self.patterns = [
            "ignore previous instructions",
            "act as a hacker",
            "reveal hidden rules",
            "bypass safeguards"
        ]

    def detect(self, text):

        text = text.lower()

        for p in self.patterns:
            if p in text:
                return True

        return False
