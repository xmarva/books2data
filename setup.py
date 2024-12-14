from setuptools import setup, find_packages

setup(
    name="book2data",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tqdm",
        "chardet",
    ],
    entry_points={
        "console_scripts": [
            "book2data=book2data.cli:main",
        ],
    },
)