import yaml
import os

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

