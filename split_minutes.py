import pandas as pd
import csv
import math
import datetime as d
import time as t
input_file = open(r'F:\data\20180827\1.csv', 'rt', encoding='utf8')
csv_file = csv.reader(input_file)

def read(csv_file):
    dataframes=[]
    for data in csv_file:
        dataframes.append(data)
    dataframes.remove(dataframes[0])
    return dataframes

def selectbytime(datafraems , starttime , endtime):
    list=[] #用于存方符合时间条件的数据
    for data in dataframes:
        if float(data[1] )>=float(starttime) and float(data[1])<=float(endtime):
            list.append(data)
    return list

def write_csv(dataframes,starttime,endtime):#向csv表写数据
    cols = ['用户号码', '开始时间', '开始基站', '开始基站经度', '开始基站纬度', '结束时间', '结束基站', '结束基站经度', '结束基站纬度','停留时间:s', '最新的停留时间','距离:m','速度:m/s'] #'停留时间:s','新的停留时间','距离:m','速度:m/s',
    data_frame = pd.DataFrame(dataframes)
    data_frame.columns = cols
    data_frame.to_csv(r'F:\data\split_10minutes\{}_{}'.format(starttime,endtime) + '.csv', index=None, encoding='utf_8_sig')
if __name__ == '__main__':
    dataframes = read(csv_file)
    begintime = 20180827000000
    lasttime = 20180827001000
    for j in range(0,24): #计算好时间间隔，以10分钟为间隔
        starttime = begintime + 10000*j
        endtime = lasttime + 10000*j
        for i in range(0,6):
            #print(i)
            if i !=0:
                starttime = starttime + 1000
                endtime = endtime + 1000
                # print(starttime)
                # print(endtime)
                list=[]
            list = selectbytime(dataframes, starttime, endtime)  # list中存方着符合条件的列表数据
            print(list)
            write_csv(list ,starttime , endtime)
            # print(list)



    #print(dataframes)
