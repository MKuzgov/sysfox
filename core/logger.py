import logging
import os

# Создание директории логов, если нет
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Настройка логгера
logger = logging.getLogger("SysFox")
logger.setLevel(logging.DEBUG)

# Форматтер
formatter = logging.Formatter("%(asctime)s — %(levelname)s — %(message)s")

# Файл логов
file_handler = logging.FileHandler(os.path.join(log_dir, "sysfox.log"))
file_handler.setFormatter(formatter)

# Консольный вывод
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Добавляем обработчики
logger.addHandler(file_handler)
logger.addHandler(console_handler)
def success(self, message):
    self.logger.info(f"✅ {message}")

