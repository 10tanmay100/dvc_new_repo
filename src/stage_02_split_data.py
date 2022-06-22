from src.utils.all_utils import read_yaml,create_directory,save_data_local
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split

def split_data(config_path,params_path):
    config=read_yaml(config_path)
    params=read_yaml(params_path)
    artifacts_dir=config["artifacts"]["artifcats_dir"]
    raw_local_dir=config["artifacts"]["raw_local_dir"]
    raw_local_file=config["artifacts"]["raw_local_file"]
    #splitting data all paths
    split_local_dir=config["artifacts"]["split_local_dir"]
    train_file=config["artifacts"]["train_file"]
    test_file=config["artifacts"]["test_file"]

    #create directory for storing splitted data
    create_directory([os.path.join(artifacts_dir,split_local_dir)])

    data_path=os.path.join(artifacts_dir,raw_local_dir,raw_local_file)
    df=pd.read_csv(data_path)
    #split the data
    train,test=train_test_split(df,test_size=params["base"]["test_size"],random_state=params["base"]["random_state"])
    #paths for train,test files
    train_file_path=os.path.join(artifacts_dir,split_local_dir,train_file)
    test_file_path=os.path.join(artifacts_dir,split_local_dir,test_file)
    #let's apply the function which converts the train and test data to csv and store it based on the path
    for data,data_path in (train,train_file_path),(test,test_file_path):
        save_data_local(data,data_path)



if __name__=="__main__":
    args=argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")

    parsed_arg=args.parse_args()

    split_data(config_path=parsed_arg.config,params_path=parsed_arg.params)
