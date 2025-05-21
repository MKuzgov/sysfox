import subprocess
from core.logger import logger

def ping_host(target: str):
    try:
        logger.info(f"📡 Pinging host: {target}")
        result = subprocess.run(['ping', '-c', '4', target], capture_output=True, text=True)
        if result.returncode == 0:
            logger.success(f"✅ Host {target} is reachable.")
            print(result.stdout)
        else:
            logger.warning(f"⚠ Host {target} is unreachable.")
            print(result.stderr)
    except Exception as e:
        logger.error(f"❌ Ping error: {str(e)}")
