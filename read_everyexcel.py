import pandas as pd
import csv
import os

#print(os.listdir(r'E:\信令数据\tmp\20180807'))
dataframes=[]
#for inputfile in os.listdir(r'E:\信令数据\tmp\20180807'):
csv_file = csv.reader(open(r'E:\信令数据\tmp\20180807\part-00137.csv', 'rt',encoding='utf8'))#{}'.format(inputfile)
    #print(csv_file)
for content in csv_file:
    if (content[0]=='11d22332-39c3-4931-b9a7-736bb8678ce0'):
        dataframes.append(content)
           #print(dataframes)


cols = ['用户号码', '开始时间', '开始基站', '开始基站经度', '开始基站纬度', '结束时间', '结束基站', '结束基站经度', '结束基站纬度', '停留时间']
data_frame = pd.DataFrame(dataframes)
data_frame.columns = cols
data_frame.to_csv(r'E:\信令数据\tmp\20180807\5test' + '.csv', index=None ,encoding = 'utf_8_sig')






