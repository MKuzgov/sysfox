import os
from datetime import datetime

def log_to_file(command, content):
    os.makedirs("logs", exist_ok=True)
    filename = f"logs/{command}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    with open(filename, 'w') as f:
        f.write(content)
    return filename
