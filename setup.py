from setuptools import setup, find_packages

setup(
    name="sysfox",
    version="0.1",
    py_modules=["main"],
    packages=find_packages(),
    install_requires=["click", "psutil", "rich"],
    entry_points={
        "console_scripts": [
            "sysfox=main:cli",
        ],
    },
)
