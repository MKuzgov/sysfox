from rich.console import Console
from rich import print
import time

console = Console()

def blink_text(text, blink_times=3, delay=0.3):
    for _ in range(blink_times):
        console.print(text, style="bold red", end="\r")
        time.sleep(delay)
        console.print(" " * len(text), end="\r")
        time.sleep(delay)
    console.print(text, style="bold red")

def print_logo():
    print("""[bold orange1]
  ┏━━━┓ ┏━━━┓ ┏━━━┓ ┏━━━┓ ┏━━━┓ ┏━━━┓
  ┃ S ┃ ┃ Y ┃ ┃ S ┃ ┃ F ┃ ┃ O ┃ ┃ X ┃
  ┗━┳━┛ ┗━┳━┛ ┗━┳━┛ ┗━┳━┛ ┗━┳━┛ ┗━┳━┛
    ╰──────╯     ╰──────╯     ╰──────╯
""")
    blink_text(">>> АКТИВИРОВАН РЕЖИМ SYSFOX <<<", blink_times=5, delay=0.15)

def print_header(title):
    print(f"\n[bold blue]=== {title.upper()} ===[/bold blue]\n")

# Пример использования
if __name__ == "__main__":
    print_logo()
    print_header("Главное меню")
