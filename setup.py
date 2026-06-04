#import the tool used to package/install the project
from setuptools import setup

#read your README file to use as project description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

#define project name, author, source folder, and needed packages
REPO_NAME = "Book-Recommendation-System-Using-Machine-Learning"
AUTHOR_NAME = "Meriam"
SRC_REP = "src"
LIST_OF_REQUIREMENTS = [
    "streamlit",
    "numpy",
    "pandas",
    "scikit-learn",
    "scipy"
]

setup(
    name=SRC_REP,
    version="0.0.1",
    author=AUTHOR_NAME,
    description="A small package for book recommendation system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    author_email="mbenarbia09@gmail.com",
    packages=[SRC_REP],
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)