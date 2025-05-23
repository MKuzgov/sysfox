from setuptools import setup, find_packages

setup(
    name="sysfox",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "rich",
        "requests",
        "psutil",
        "python-whois"
    ],
    entry_points={
        'console_scripts': [
            'sysfox=main:main'
        ]
    },
    author="Your Name",
    description="SysFox - Powerful Network Toolkit",
    keywords="network security tools cli sysadmin",
)
