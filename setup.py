from setuptools import find_packages, setup

setup(
    name = "MCQ_Generator",
    version = "0.0.1",
    author = "Cks1210",
    author_email = "kaisin1993@hotmail.com",
    install_requires = ['openai','langchain', 'streamlit', 'python-dotenv', 'PyPDF2'],
    packages = find_packages()
)