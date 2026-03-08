import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/safeguard.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_attack(message):
    logging.warning(message)

def log_safe(message):
    logging.info(message)