
from gateway.llm_firewall import LLMFirewall
from moderation.prompt_attack_detector import PromptAttackDetector
from moderation.toxicity_detector import ToxicityDetector
from moderation.contextual_reasoning import ContextAnalyzer
from pipeline.realtime_pipeline import ModerationPipeline

def main():

    firewall = LLMFirewall()
    attack = PromptAttackDetector()
    tox = ToxicityDetector()
    ctx = ContextAnalyzer()

    pipeline = ModerationPipeline(firewall, attack, tox, ctx)

    print("AI Safety Platform running. type exit to quit")

    while True:

        text = input("Input: ")

        if text.lower() == "exit":
            break

        result = pipeline.process(text)

        print(result)

if __name__ == "__main__":
    main()
