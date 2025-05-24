from datetime import datetime
import os
from sysfox.core.logger import setup_logger

logger = setup_logger()

LOG_FILE = "logs/sysfox.log"
HISTORY_FILE = "logs/command_history.log"

def save_report(command, output):
    folder = "reports"
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{folder}/{command}_{timestamp}.txt"
    with open(filename, "w") as file:
        file.write(output)
    logger.info(f"[REPORT] Сохранён в файл: {filename}")
    return filename

def log_command(command):
    os.makedirs("logs", exist_ok=True)
    with open(HISTORY_FILE, "a") as f:
        f.write(f"{datetime.now()} :: {command}\n")

def get_last_commands(n=3):
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        lines = f.readlines()
        return lines[-n:]

def get_logs_for_commands(commands):
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        log_lines = f.readlines()
    filtered_logs = []
    for cmd in commands:
        keyword = cmd.split("::")[-1].strip()
        matching = [line for line in log_lines if keyword in line]
        filtered_logs.extend(matching)
    return filtered_logs

def create_auto_report():
    from rich import print
    from modules.network.utils import print_logo, print_header

    print_logo()
    print_header("Automatic Report")

    last_cmds = get_last_commands()
    logs = get_logs_for_commands(last_cmds)

    text = "[SYSFOX AUTO REPORT]\n\n"
    text += "🕹️ Последние команды:\n"
    text += "".join(last_cmds) + "\n"
    text += "📄 Связанные логи:\n"
    text += "".join(logs)

    filename = save_report("auto", text)
    print(f"[bold green]✔ Автоотчёт сохранён:[/bold green] {filename}")


