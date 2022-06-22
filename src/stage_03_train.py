from operator import mod
from pyexpat import model
from venv import create
from idna import check_nfc
from src.utils.all_utils import read_yaml,create_directory,save_data_local
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import joblib

def split_data(config_path,params_path):
    config=read_yaml(config_path)
    params=read_yaml(params_path)
    #splitting data all paths
    artifacts_dir=config["artifacts"]["artifcats_dir"]
    split_local_dir=config["artifacts"]["split_local_dir"]
    train_file=config["artifacts"]["train_file"]
    test_file=config["artifacts"]["test_file"]
    model_local_dir=config["artifacts"]["model_local_dir"]
    model_file=config["artifacts"]["model_file"]

    #create directory for model
    create_directory([os.path.join(artifacts_dir,model_local_dir)])
    #path of storing model
    model_file_path=os.path.join(artifacts_dir,model_local_dir,model_file)

    #paths for train files
    train_file_path=os.path.join(artifacts_dir,split_local_dir,train_file)
    #read the data for training
    train_data=pd.read_csv(train_file_path)
    #using the model
    lr=ElasticNet(alpha=params["model_params"]["ElasticNet"]["alpha"],l1_ratio=params["model_params"]["ElasticNet"]["l1_ratio"])
    x_train=train_data.drop("quality",axis=1)
    y_train=train_data["quality"]
    #fitting the model
    lr.fit(x_train,y_train)
    joblib.dump(lr,model_file_path)

if __name__=="__main__":
    args=argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")

    parsed_arg=args.parse_args()

    split_data(config_path=parsed_arg.config,params_path=parsed_arg.params)