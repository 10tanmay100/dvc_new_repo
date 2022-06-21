from src.utils.all_utils import read_yaml,create_directory
import argparse
import pandas as pd
import os

def get_data(config_path):
    config=read_yaml(config_path)
    df=pd.read_csv(config["data_source"],delimiter=";")
    #creating directory from config files for files to save it in local
    artifacts_dir=config["artifacts"]["artifcats_dir"]
    raw_local_dir=config["artifacts"]["raw_local_dir"]
    raw_local_file=config["artifacts"]["raw_local_file"]
    #create a directory
    raw_local_dir_path=os.path.join(artifacts_dir,raw_local_dir)
    #adding data in csv directory
    create_directory(dirs=[raw_local_dir_path])
    #creating csv file for the data
    raw_local_file_path=os.path.join(raw_local_dir_path,raw_local_file)
    #now convert to csv
    df.to_csv(raw_local_file_path,sep=",",index=False)






if __name__=="__main__":
    args=argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")

    parsed_arg=args.parse_args()

    get_data(config_path=parsed_arg.config)









