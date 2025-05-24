from datetime import datetime
import os
from sysfox.core.logger import setup_logger

logger = setup_logger()

def save_report(command, output):
    folder = "reports"
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{folder}/{command}_{timestamp}.txt"
    with open(filename, "w") as file:
        file.write(output)
    logger.info(f"[REPORT] Отчет сохранен: {filename}")
    return filename
