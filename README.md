# SysFox — Universal Linux Utility for Admins, DevOps, and Security Engineers

SysFox — это мощная, модульная утилита для системных администраторов, DevOps-инженеров, специалистов по кибербезопасности и сетевому анализу. Инструмент включает CLI, AI, GUI и Web API — всё в одном.

---

## Возможности

- **Сетевой аудит**: пинг, трассировка, сканирование сети, открытые порты
- **Анализ безопасности**: проверка фаервола, открытых портов, вредоносных процессов
- **Автоматизация**: автоматическая постустановка Linux, скрипты cron/systemd
- **AI Анализатор**: анализ логов, предсказания сбоев и угроз, автоотчеты
- **Системная информация**: нагрузка CPU, RAM, диски, установленные пакеты
- **Отчеты**: логирование, html/pdf-отчеты
- **Интерфейсы**: CLI, GUI (PyQt), Web API (FastAPI)
- **Упаковка**: AppImage, DEB, portable

---

## Установка

```bash
git clone https://github.com/yourname/sysfox.git
cd sysfox
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py

