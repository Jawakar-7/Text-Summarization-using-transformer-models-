"""
template.py  file is used to create a template for our project , instead of creating files and folders manually , 
we will write a pythonfile to simplify this process. 
"""
import os 
from pathlib import Path
import logging 
#to log all the information during login 

logging.basicConfig(level=logging.info,format='[%(asctime)s]:%(message)s:')

project_name="textSummarizer"

list_of_files=[
    ".github/workflows/.gitkeep",#helps to do CI/CD deployment . whenever we commit the code in github it automatically deploys it in the cloud 
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/login/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"

]


for fpath in list_of_files:
    fpath=Path(fpath) # used to change the file path according to windows format
    filedir,filename=os.path.split(fpath) # the function returns directory and file name if a file path is given in a tuple .

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory :{filedir} for the file {filename}")

    if (not os.path.exists(fpath)) or (os.path.getsize(fpath)==0):
        with open (fpath,'w') as f:
            pass 
            logging.info(f"Creating empty file : {fpath}")
    else:
        logging.info(f"{filename} is already exists")
    





