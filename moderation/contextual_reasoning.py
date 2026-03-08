
class ContextAnalyzer:

    def analyze(self, text):

        context = {}

        t = text.lower()

        if "bomb" in t:
            if "history" in t:
                context["type"] = "educational"
            else:
                context["type"] = "potential_threat"
        else:
            context["type"] = "normal"

        return context
