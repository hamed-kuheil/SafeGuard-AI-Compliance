
from transformers import pipeline

class ToxicityDetector:

    def __init__(self):

        self.model = pipeline(
            "text-classification",
            model="unitary/toxic-bert"
        )

    def detect(self, text):

        result = self.model(text)[0]

        return {
            "label": result["label"],
            "score": result["score"]
        }
