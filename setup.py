import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()



__version__="0.0.0"

REPO_NAME="Text-Summarization-using-transformer-models"
AUTHOR_USER_NAME="Jawakar-7"
SRC_REPO="Text-Summarization-using-transformer-models"
AUTHOR_EMAIL="jawakardn@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A NLP project for text summarization",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)

#setuptools is a Python library that provides utilities for packaging, distributing, and installing Python projects. 
# It is commonly used to define the metadata and dependencies of a project and create distributable packages such as source distributions
#  (.tar.gz files) and binary distributions (.whl files).