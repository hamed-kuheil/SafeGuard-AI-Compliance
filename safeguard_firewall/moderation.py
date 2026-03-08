BANNED_WORDS = [
    "kill",
    "bomb",
    "terror",
    "hack",
    "exploit"
]

def moderate_text(text: str):
    text = text.lower()
    for word in BANNED_WORDS:
        if word in text:
            return False
    return True