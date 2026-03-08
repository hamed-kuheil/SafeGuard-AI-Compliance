INJECTION_PATTERNS = [
    "ignore previous instructions",
    "reveal system prompt",
    "bypass safety",
    "act as developer",
    "system override",
    "jailbreak",
    "developer mode",
    "pretend you are"
]

def detect_prompt_injection(prompt: str):
    prompt = prompt.lower()
    for pattern in INJECTION_PATTERNS:
        if pattern in prompt:
            return True
    return False