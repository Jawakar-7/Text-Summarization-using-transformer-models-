# implements oops concept , here we write a frequently used function in our application and 
# invoke it instead of writing it again and again



import os
from box.exceptions import BoxValueError
#catching exceptions in a box refers to catching multiple exceptions using a single except block, 
#reducing code duplication and improving readability.
import yaml
# YAML (YAML Ain't Markup Language) is a human-readable data serialization format. It stands out for its simplicity
# and readability, making it popular for configuration files, data exchange, and structured data representation.
#  YAML is often used in various programming languages and applications to represent data in a concise and easily understandable manner.

from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import config_box
#config box is similar to a dictionary where as in dictionary you can
# access a value by giving a key like this => dict['key']= value . but when you give like this dict.key => it will show erroe 
# so to bypass this we have condig box . d2=config_box('key'='value') , d2.'key' returns => 'value
# here config box is used to retrive Yaml files 
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """ read yaml file and returns
    Args:
         path_to_yaml(str):path like input

    Raises:
         ValueError:if yaml file is empty
         e:empty file
    Returns:
         ConfiBox:ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml}loaded succesfully")
            return config_box(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories
    Args:
         path_to_directories(list):list of path of directories
         ignore_log(bool,optional ):ignore if ultiple dirs is to be created . Defaults to false.
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at : {path}")



@ensure_annotations
def get_size(path:Path)->str:
    """get size in KB
    
    Args:
         path (Path):path of file
    Returns:
         str:size in KB
    """
    size_in_kb=round(os.path.getsize(path/1024))
    return f"~{size_in_kb}KB"