import pandas as pd
import os
import re

def zup():

    pose3dname = os.listdir("pose-3d")[0]
    matches = re.findall(r"\d+", pose3dname)
    numbers = [int(match) for match in matches]

    filename = f'pose-3d/Video2Sim_filt_{numbers[1]}-{numbers[2]}.trc'
    # 使用read_csv函数读取TRC文件的前四行（元数据）
    with open(filename, 'r') as file:
        metadata = [next(file) for _ in range(4)]


    # 使用read_csv函数读取文件，跳过前4行
    dataframe = pd.read_csv(filename, skiprows=4, delimiter='\t')

    for key in dataframe.keys():
        if 'Y' in key:
            dataframe[key]=-dataframe[key]
        if 'Z' in key:
            dataframe[key]=-dataframe[key]

    dataframe = dataframe.rename(columns={"Unnamed: 0": "", "Unnamed: 1": ""})
    tempfilename=f'pose-3d/test_{numbers[1]}-{numbers[2]}.trc'

    # 将元数据和修改后的DataFrame写回TRC文件
    with open(tempfilename, 'w') as file:
        file.writelines(metadata)
        dataframe.to_csv(file, sep='\t', index=False)

zup()