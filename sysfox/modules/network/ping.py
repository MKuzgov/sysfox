import subprocess
from rich import print
from modules.network.utils import print_header, print_logo
from sysfox.core.logger import setup_logger

logger = setup_logger()

def ping_host(target, count):
    print_logo()
    print_header("Ping")
    logger.info(f"[PING] Ping до {target}, count={count}")
    try:
        result = subprocess.run(["ping", "-c", str(count), target], capture_output=True, text=True)
        print(result.stdout)
        logger.info(f"[PING] Ping завершен для {target}")
    except Exception as e:
        print(f"[bold red]Error:[/bold red] {str(e)}")
        logger.error(f"[PING] Ошибка: {e}")
