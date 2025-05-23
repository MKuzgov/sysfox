from rich import print

def print_logo():
    print("""[bold orange1]
  ┏━━━┓ ┏━━━┓ ┏━━━┓ ┏━━━┓ ┏━━━┓ ┏━━━┓
  ┃ S ┃ ┃ Y ┃ ┃ S ┃ ┃ F ┃ ┃ O ┃ ┃ X ┃
  ┗━┳━┛ ┗━┳━┛ ┗━┳━┛ ┗━┳━┛ ┗━┳━┛ ┗━┳━┛
    ╰──────╯     ╰──────╯     ╰──────╯
""")
def print_header(title):
    print(f"\n[bold blue]=== {title.upper()} ===[/bold blue]\n")
