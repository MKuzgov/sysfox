import psutil
from core.logger import logger

def list_interfaces():
    logger.info("🌐 Получение сетевых интерфейсов...")
    interfaces = psutil.net_if_addrs()
    for name, addresses in interfaces.items():
        logger.success(f"🔸 Интерфейс: {name}")
        for addr in addresses:
            print(f"    {addr.family.name}: {addr.address}")
