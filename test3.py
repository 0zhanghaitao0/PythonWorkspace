import pandas as pd
import csv
import math
import datetime as d
import time as t
input_file = open(r'E:\信令数据\tmp\20180827\part-00000.csv', 'rt', encoding='utf8')
csv_file = csv.reader(input_file)
def scan_alldoucument(csv_file):
    data=[]
    dataframes=[] #存储了所有用户的数据
    list=[]
    for content in csv_file:
        dataframes.append(content)
    dataframes=remove_noise_1(dataframes)
    return dataframes

def remove_noise_1(dataframes):
    length = len(dataframes)
    m=1
    while m < length:
        if float(dataframes[m][3])==0 or float(dataframes[m][7])==0:
            dataframes.remove(dataframes[m])
            length=len(dataframes)
        else:
            m=m+1
    return dataframes

def write_csv(dataframes):
    cols = ['用户号码', '开始时间', '开始基站', '开始基站经度', '开始基站纬度', '结束时间', '结束基站', '结束基站经度', '结束基站纬度', '停留时间']
    data_frame = pd.DataFrame(dataframes)
    data_frame.columns = cols
    data_frame.to_csv(r'E:\信令数据\tmp\20180827\aaa' + '.csv', index=None, encoding='utf_8_sig')


if __name__ == '__main__':
    dataframes = scan_alldoucument(csv_file)
    write_csv(dataframes)