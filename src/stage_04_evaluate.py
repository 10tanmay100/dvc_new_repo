from src.utils.all_utils import read_yaml,create_directory,save_data_local
import argparse
import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import joblib
from sklearn.metrics import mean_absolute_error,r2_score

def evaluation_metrics(actual,pred):
    mae=round(mean_absolute_error(actual,pred),2)
    rmae=round(np.sqrt(mae),2)
    r2=round(r2_score(actual,pred),2)
    return mae,rmae,r2




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

    #path of storing model
    model_file_path=os.path.join(artifacts_dir,model_local_dir,model_file)

    #paths for test files
    test_file_path=os.path.join(artifacts_dir,split_local_dir,train_file)
    #read the data for test
    test_data=pd.read_csv(test_file_path)
    #using the model
    x_test=test_data.drop("quality",axis=1)
    y_test=test_data["quality"]
    #prediction the model
    model=joblib.load(model_file_path)
    predicted_data=model.predict(x_test)
    mae,rmae,r2=evaluation_metrics(y_test,predicted_data)
    print(mae,rmae,r2)


if __name__=="__main__":
    args=argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")

    parsed_arg=args.parse_args()

    split_data(config_path=parsed_arg.config,params_path=parsed_arg.params)