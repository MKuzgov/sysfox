import whois
from rich import print
from rich.panel import Panel
from rich.markdown import Markdown
from modules.network.utils import print_header, print_logo
from sysfox.core.logger import setup_logger

logger = setup_logger()

def whois_lookup(domain):
    print_logo()
    print_header("Whois Lookup")
    logger.info(f"[WHOIS] Запрос WHOIS для {domain}")
    try:
        result = whois.whois(domain)
        if isinstance(result, dict):
            text = "\n".join(f"**{k}**: {v}" for k, v in result.items() if v)
            print(Panel(Markdown(text), title=f"WHOIS for {domain}"))
        else:
            print(result)
        logger.info(f"[WHOIS] Успешный результат для {domain}")
    except Exception as e:
        print(f"[bold red]Error:[/bold red] {str(e)}")
        logger.error(f"[WHOIS] Ошибка: {e}")
