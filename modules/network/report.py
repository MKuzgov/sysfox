# modules/network/report.py
import os
from datetime import datetime


def generate_report():
    logs = os.listdir("logs")
    report_path = f"logs/report_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.md"

    with open(report_path, "w") as report:
        report.write("# SysFox Network Report\n\n")
        for log_file in logs:
            if log_file.endswith(".log"):
                report.write(f"## {log_file}\n")
                with open(f"logs/{log_file}", "r") as lf:
                    report.write("```\n" + lf.read() + "\n```\n\n")
    return report_path
