from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os


def generate_report(stats: dict, filename: str = "sysfox_report"):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")

    rendered = template.render(stats=stats)
    os.makedirs("reports", exist_ok=True)

    html_path = f"reports/{filename}.html"
    pdf_path = f"reports/{filename}.pdf"

    with open(html_path, "w") as f:
        f.write(rendered)

    HTML(html_path).write_pdf(pdf_path)
    return html_path, pdf_path
