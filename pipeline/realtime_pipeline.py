
class ModerationPipeline:

    def __init__(self, firewall, attack_detector, toxicity, context):

        self.firewall = firewall
        self.attack_detector = attack_detector
        self.toxicity = toxicity
        self.context = context

    def process(self, text):

        fw = self.firewall.inspect(text)

        if fw["blocked"]:
            return {"status": "blocked", "reason": fw["reason"]}

        if self.attack_detector.detect(text):
            return {"status": "blocked", "reason": "prompt injection"}

        tox = self.toxicity.detect(text)
        context = self.context.analyze(text)

        if tox["score"] > 0.85:
            return {"status": "blocked", "reason": "high toxicity"}

        return {
            "status": "allowed",
            "analysis": {
                "toxicity": tox,
                "context": context
            }
        }
