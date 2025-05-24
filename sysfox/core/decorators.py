# core/decorators.py

from functools import wraps
from sysfox.core.logger import setup_logger
import traceback

logger = setup_logger()

def log_command(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"[+] Запуск: {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"[✓] Успешно завершено: {func.__name__}")
            return result
        except Exception as e:
            logger.error(f"[!] Ошибка в {func.__name__}: {e}")
            logger.debug(traceback.format_exc())
            raise
    return wrapper
