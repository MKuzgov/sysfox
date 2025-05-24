# modules/ai/diagnostic.py
import subprocess
from sysfox.core.logger import setup_logger

logger = setup_logger()

def analyze_error(traceback_str):
    prompt = (
        "Ты — ИИ-помощник по отладке. Пользователь получил следующую ошибку:\n\n"
        f"{traceback_str}\n\n"
        "Объясни кратко, что произошло и как исправить."
    )

    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt,
            text=True,
            capture_output=True,
            timeout=30
        )
        answer = result.stdout.strip()
        logger.info("[AI] Ответ AI:\n" + answer)
        return answer
    except Exception as e:
        logger.error(f"[AI] Ошибка анализа: {e}")
        return "AI анализ не удалось выполнить."
