import glob
import os
import pandas as pd
import numpy as np

def read_files(folder_name, output_filename,file_extension,sheet_name):
    rec_file_names = [file for file in os.listdir(folder_name) if file.endswith(file_extension)]
    print(rec_file_names)
    dataframes = []
    for filename in rec_file_names:
        if file_extension == 'csv':
            df = pd.read_csv(os.path.join(folder_name, filename),low_memory=False)
        elif file_extension == 'xlsx':
            df = pd.read_excel(os.path.join(folder_name, filename), sheet_name=sheet_name)
        df = df.astype(str)
        dataframes.append(df)
        data_concated = pd.concat(dataframes, axis=0)
        print('df_shape',data_concated.shape)
        data_concated.to_parquet(output_filename)
        
        
output_filename = r'filename.parquet'
folder_name = r'folder_path'
read_files(folder_name,output_filename,file_extension='csv',sheet_name=None)
