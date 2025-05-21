# modules/network/utils.py
import os
from datetime import datetime

LOG_DIR = "logs"


def save_log(command_name: str, output: str):
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{LOG_DIR}/{command_name}_{timestamp}.log"
    with open(filename, "w") as f:
        f.write(output)

    return filename
