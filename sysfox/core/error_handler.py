# sysfox/core/error_handler.py

import sys
import traceback
from rich import print
from sysfox.core.logger import setup_logger

logger = setup_logger()

def handle_uncaught_exceptions(exc_type, exc_value, exc_traceback):
    """Обработка всех необработанных исключений"""
    if issubclass(exc_type, KeyboardInterrupt):
        print("[bold yellow]Программа прервана пользователем[/bold yellow]")
        logger.warning("Пользователь завершил программу вручную")
        return

    logger.error("Неперехваченная ошибка", exc_info=(exc_type, exc_value, exc_traceback))
    print(f"\n[bold red]Произошла ошибка: {exc_value}[/bold red]")
    print("[italic]Подробности записаны в лог[/italic]")

# Привязка обработчика
sys.excepthook = handle_uncaught_exceptions
from modules.ai.diagnostic import analyze_error

def handle_uncaught_exceptions(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        print("[bold yellow]Программа прервана пользователем[/bold yellow]")
        logger.warning("Пользователь завершил программу вручную")
        return

    import traceback
    traceback_str = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))

    logger.error("Неперехваченная ошибка", exc_info=(exc_type, exc_value, exc_traceback))
    print(f"\n[bold red]Произошла ошибка: {exc_value}[/bold red]")
    print("[italic]Подробности записаны в лог[/italic]")

    ai_response = analyze_error(traceback_str)
    print("\n[bold green]AI-помощник:[/bold green]\n" + ai_response)

sys.excepthook = handle_uncaught_exceptions
