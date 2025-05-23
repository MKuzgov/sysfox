from datetime import datetime
import os

def save_report(command, output):
    folder = "reports"
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{folder}/{command}_{timestamp}.txt"
    with open(filename, "w") as file:
        file.write(output)
    return filename
