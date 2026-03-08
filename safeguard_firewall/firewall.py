from .prompt_detector import detect_prompt_injection
from .sensitive_data import detect_sensitive_data
from .risk_score import calculate_risk
from .moderation import moderate_text
from .logger import log_attack, log_safe

def firewall_scan(prompt):

    risk = calculate_risk(prompt)

    if detect_prompt_injection(prompt):

        log_attack("Prompt Injection detected")

        return {
            "allowed": False,
            "reason": "Prompt Injection",
            "risk_score": risk
        }

    if detect_sensitive_data(prompt):

        log_attack("Sensitive data detected")

        return {
            "allowed": False,
            "reason": "Sensitive Data",
            "risk_score": risk
        }

    if not moderate_text(prompt):

        log_attack("Unsafe content")

        return {
            "allowed": False,
            "reason": "Unsafe Content",
            "risk_score": risk
        }

    log_safe("Prompt allowed")

    return {
        "allowed": True,
        "risk_score": risk
    }