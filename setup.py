from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'Team 4'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']  


setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = AUTHOR_NAME,
    package = [SRC_REPO],
    pyhton_requires = '>=3.7',
    install_requires = LIST_OF_REQUIREMENTS
)