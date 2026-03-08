from .prompt_detector import detect_prompt_injection
from .sensitive_data import detect_sensitive_data

def calculate_risk(prompt: str):

    score = 0

    if detect_prompt_injection(prompt):
        score += 0.6

    if detect_sensitive_data(prompt):
        score += 0.4

    return score