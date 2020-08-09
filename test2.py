#按时间段读出数据
import csv
import pandas as pd
input_file = open(r'E:\信令数据\tmp\20180827\part-00000_x.csv', 'rt', encoding='utf8')
csv_file = csv.reader(input_file)

def scan_alldoucument(csv_file):
    data=[]
    dataframes=[] #存储了所有用户的数据
    list=[]
    for content in csv_file:
        dataframes.append(content)
    for i in range(1 , len(dataframes)-1):
        if dataframes[i][0] == dataframes[i+1][0]:
            list.append(dataframes[i])
        else:
            list.append(dataframes[i])
            data.append(list)
            list=[]

    print(len(data))
    return data

def select_time(dataframes,t1,t2):
    data=[]
    for content in dataframes:
        for content1 in content:
            if  int(content1[1])<=t2 and int(content1[1]) >= t1:
                data.append(content1)
    return data

def write_csv(dataframes):#向csv表写数据
    cols = ['用户号码', '开始时间', '开始基站', '开始基站经度', '开始基站纬度', '结束时间', '结束基站', '结束基站经度', '结束基站纬度', '停留时间:s','最新的停留时间','距离:m','速度:m/s'] #,'距离:m','速度:m/s'
    data_frame = pd.DataFrame(dataframes)
    data_frame.columns = cols
    data_frame.to_csv(r'E:\信令数据\tmp\20180827\part-00000_xx' + '.csv', index=None, encoding='utf_8_sig')

if __name__ == '__main__':
    t1 = 20180827060000
    t2 = 20180827120000
    dataframes = scan_alldoucument(csv_file)
    dataframes = select_time(dataframes,t1,t2)
    write_csv(dataframes)