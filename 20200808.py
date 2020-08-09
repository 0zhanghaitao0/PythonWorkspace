import pandas as pd
import csv
import math
import datetime
import time as t
from datetime import datetime

input_file = open(r'F:\data\20180827\part-00000.csv', 'rt', encoding='utf8')
csv_file = csv.reader(input_file)

#读取数据，返回数据列表datasList
def readData(csv_file):
    datasList=[]
    for data in csv_file:
        datasList.append(data)
    datasList.remove(datasList[0]) #去除第一行中文标识
    return datasList

#去除起始基站经纬度或结束基站经纬度为0的数据
def deleteZeroData(datasList):
    deleteList=[] #存储将要删除的数据即经纬度为0的数据
    for data in datasList:
        if float(data[3])== 0 or float(data[4])==0 or float(data[7])==0 or float(data[8])== 0:
            deleteList.append(data)
    for data in deleteList:
        datasList.remove(data)
    return datasList

#根据用户号码为分类出不同的用户
def groupByUserId(datasList):
    list1=[]
    dataGroupsList=[] #存储不同用户的信令数据
    list=[] #中间列表
    for i in range(0 , len(datasList)-1):
        print(len(datasList))

        if datasList[i][0] == datasList[i+1][0]:
            list.append(datasList[i])
        else:
            list.append(datasList[i])
            dataGroupsList.append(list)
            list=[]
    #添加上最后一组用户的数据
    index = datasList.index(dataGroupsList[-1][-1])
    list=[]
    for i in range(index+1 , len(datasList)):
        list.append(datasList[i])
    dataGroupsList.append(list)
    # for data in dataGroupsList:
    #     for i in data:
    #         list1.append(i)
    # print(len(list1))
    return dataGroupsList




def write_csv(datasList):#向csv表写数据
    cols = ['用户号码', '开始时间', '开始基站', '开始基站经度', '开始基站纬度', '结束时间', '结束基站', '结束基站经度', '结束基站纬度','停留时间']
    datas_List = pd.DataFrame(datasList)
    datas_List.columns = cols
    datas_List.to_csv(r'F:\data\20180827\2' + '.csv', index=None, encoding='utf_8_sig')

if __name__ == '__main__':
    datasList = readData(csv_file) #读取数据,datasList为接收的数据列表
    datasList = deleteZeroData(datasList) #删除经纬度为0的数据
    dataGroupsList = groupByUserId(datasList) #根据用户号码为分类出不同的用户
    write_csv(datasList)





