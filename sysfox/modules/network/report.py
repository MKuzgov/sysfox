from datetime import datetime
import os
import subprocess

LOG_FILE = "logs/sysfox.log"
HISTORY_FILE = "logs/command_history.log"

from sysfox.core.logger import setup_logger
logger = setup_logger()

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
    from datetime import datetime
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        log_lines = f.readlines()
    timestamps = []
    for line in commands:
        try:
            ts_str = line.split("::")[0].strip()
            timestamps.append(datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S.%f"))
        except:
            continue
    filtered_logs = []
    for ts in timestamps:
        for log in log_lines:
            try:
                log_ts_str = log.split(" — ")[0].strip()
                log_ts = datetime.strptime(log_ts_str, "%Y-%m-%d %H:%M:%S,%f")
                if log_ts >= ts:
                    filtered_logs.append(log)
            except:
                continue
    return filtered_logs

def get_outputs_for_commands(commands):
    outputs = []
    for cmd_line in commands:
        cmd = cmd_line.split("::")[-1].strip()
        full_cmd = f"sysfox {cmd}"
        try:
            result = subprocess.run(full_cmd.split(), capture_output=True, text=True)
            outputs.append(f"$ {full_cmd}\n{result.stdout}\n{result.stderr}\n")
        except Exception as e:
            outputs.append(f"$ {full_cmd}\nОшибка запуска: {e}\n")
    return outputs

def create_auto_report():
    from rich import print
    from modules.network.utils import print_logo, print_header

    print_logo()
    print_header("Automatic Report")

    last_cmds = get_last_commands()
    logs = get_logs_for_commands(last_cmds)
    outputs = get_outputs_for_commands(last_cmds)

    text = "[SYSFOX AUTO REPORT]\n\n"
    text += "🕹️ Последние команды:\n"
    text += "".join(last_cmds) + "\n"
    text += "📤 Вывод команд:\n"
    text += "".join(outputs) + "\n"
    text += "📄 Связанные логи:\n"
    text += "".join(logs)

    filename = save_report("auto", text)
    print(f"[bold green]✔ Автоотчёт сохранён:[/bold green] {filename}")
