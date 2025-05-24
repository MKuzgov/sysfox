import subprocess
from rich import print
from modules.network.utils import print_header, print_logo
from sysfox.core.logger import setup_logger

logger = setup_logger()

def traceroute(target):
    print_logo()
    print_header("Traceroute")
    logger.info(f"[TRACE] Traceroute до {target}")
    try:
        result = subprocess.run(["traceroute", target], capture_output=True, text=True)
        print(result.stdout)
        logger.info(f"[TRACE] Traceroute завершен для {target}")
    except Exception as e:
        print(f"[bold red]Error:[/bold red] {str(e)}")
        logger.error(f"[TRACE] Ошибка: {e}")
