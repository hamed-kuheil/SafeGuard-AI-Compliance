import re

EMAIL_PATTERN = r"\S+@\S+"
API_KEY_PATTERN = r"sk-[A-Za-z0-9]{20,}"
CREDIT_CARD_PATTERN = r"\b(?:\d[ -]*?){13,16}\b"

def detect_sensitive_data(text: str):

    if re.search(EMAIL_PATTERN, text):
        return True

    if re.search(API_KEY_PATTERN, text):
        return True

    if re.search(CREDIT_CARD_PATTERN, text):
        return True

    return False