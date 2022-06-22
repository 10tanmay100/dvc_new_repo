from textwrap import indent
import yaml
import os
import json


def read_yaml(path_to_yaml:str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content= yaml.safe_load(yaml_file)

    return content


def create_directory(dirs:list):
    for dirs_path in dirs:
        os.makedirs(dirs_path,exist_ok=True)
        print("Directory created for data!!")


def save_data_local(data,data_path):
    data.to_csv(data_path)
    print(f"Data Stored in {data_path}")

def store_score(data:dict,data_path:str):
    with open(data_path,"w") as f:
        json.dump(data,f,indent=4)
    print(f"FIle Saved at {data_path}")