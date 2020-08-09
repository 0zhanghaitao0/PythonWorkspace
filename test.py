#添加热力图所需的权值
import csv
import pandas as pd
input_file = open(r'E:\信令数据\tmp\20180827\part-00000_x4.csv', 'rt', encoding='utf8')
csv_file = csv.reader(input_file)

def read_excel(csv_file):   #csv文件，存入列表dataframes
    dataframes = []
    for content in csv_file:
        dataframes.append(content)
    dataframes.remove(dataframes[0])
    return dataframes

def data_process(dataframes):
    length = len(dataframes)
    m=0
    while (m < length):
        count = 1

        n = m+1
        while ( n < length):
            if float(dataframes[n][3]) == float(dataframes[m][3]) and float(dataframes[n][4]) == float(dataframes[m][4]):
                if float(dataframes[n][7]) == float(dataframes[m][7]) and float(dataframes[n][8]) == float(dataframes[m][8]):
                    count = count + 1
                    dataframes.remove(dataframes[n])
                    length = len(dataframes)
            n = n +1
        dataframes[m].append(count)
        m=m+1
    return dataframes


def write_csv(dataframes):#向csv表写数据
    cols = ['用户号码', '开始时间', '开始基站', '开始基站经度', '开始基站纬度', '结束时间', '结束基站', '结束基站经度', '结束基站纬度', '停留时间:s','最新的停留时间','距离:m','速度:m/s' ,'出现次数'] #,'距离:m','速度:m/s'
    data_frame = pd.DataFrame(dataframes)
    data_frame.columns = cols
    data_frame.to_csv(r'E:\信令数据\tmp\20180827\part-00000_xx4' + '.csv', index=None, encoding='utf_8_sig')


if __name__ == '__main__':
    dataframes = read_excel(csv_file)
    dataframes = data_process(dataframes)
    write_csv(dataframes)

