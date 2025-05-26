from setuptools import setup, find_packages

setup(
    name="sysfox",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "rich",
        "requests",
        "psutil",
        "whois",
        "scapy",
    ],
    entry_points={
        "console_scripts": [
            "sysfox = sysfox.main:main",
        ],
    },
)
