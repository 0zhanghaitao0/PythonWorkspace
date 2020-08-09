#以固定格式输出，点标记图，折线图
import xlrd
import csv
def read_excel(dirname):
    list=[]

    dataframes=[]
    f = csv.reader(open(dirname, 'r',encoding='UTF-8'))
    for data in f:
        dataframes.append(data)
    dataframes.remove(dataframes[0])
    #print(dataframes)
    for data in dataframes:
        list1 = []
        list1.append(float(data[4]))
        list1.append(float(data[3]))
        list.append(list1)
    #print(list)
    return list

    #workBook = xlrd.open_workbook(dirname)
    # 1.获取sheet的名字
    # 1.1 获取所有sheet的名字(list类型)
    ##allSheetNames = workBook.sheet_names()
    #print(allSheetNames)
    # 1.2 按索引号获取sheet的名字（string类型）
    ##sheet1Name = workBook.sheet_names()[0]
    #print(sheet1Name)
    ## 2.2 法2：按sheet名字获取sheet内容
    ##sheet1_content2 = workBook.sheet_by_name('320106')
    # 3. sheet的名称，行数，列数
    #print(sheet1_content2.name, sheet1_content2.nrows, sheet1_content2.ncols)
    # 4. 获取整行和整列的值（数组）
    #rows = sheet1_content2.row_values(3)  # 获取第四行内容
    #cols = sheet1_content2.col_values(2)  # 获取第三列内容
    #print(rows)
    # list=[]
    # for  i in range(1,sheet1_content2.nrows):
    #     list1=[]
    #     list1.append(sheet1_content2.cell(i, 2).value)
    #     list1.append(sheet1_content2.cell(i, 1).value)
    #     # list1.append(int(sheet1_content2.cell(i, 5).value%1000000))
    #     #list1.append("circle")
    #     list.append(list1)

    #print(list)
    #return list
def list_to_dict(list):#列表转换成指定格式
    list3=[]
    for list1 in list:
        #print(list1)
        list2 = ['lat','lng']
        d = {}
        for i in range(len(list2)):
            d[list2[i]]=list1[i]
            list3.append(d)
    return list3
def format(list_read_excel): #按固定的格式输出，目的是方便使用JSapi 打点和标注
    list=[]
    for content in list_read_excel:
        #print(content)
        str = "new BMapGL.Point({},{}),".format(content[1],content[0])
        #print("new BMapGL.Point({},{}),".format(content[1],content[0]))
        list.append(str)
    return list

def write(list1):
    f = "F:\data\ddd.txt"
    with open(f, "a+") as file:  # ”w"代表着每次运行都覆盖内容
        for data in list1:
            for info in data:
                file.write(str(info)+ "\n")

def getdirname(starttime , endtime): #获取到每个文件的名字
    return "F:\data\split_10minutes\{}_{}".format(starttime,endtime)+ ".csv"

if __name__ == '__main__':
    begintime = 20180827000000
    lasttime = 20180827001000

    for j in range(0, 24):  # 计算好时间间隔，以10分钟为间隔
        starttime = begintime + 10000 * j
        endtime = lasttime + 10000 * j
        for i in range(0, 6):
            list1 = []
            list2=[]
            # print(i)
            if i != 0:
                starttime = starttime + 1000
                endtime = endtime + 1000
            dirname = getdirname(starttime,endtime) #获取文件名
            list_read_excel = read_excel(dirname) #读出文件数据
            #print(list_read_excel)
    #list_dict = list_to_dict(list_read_excel)
            list = format(list_read_excel)
            # list1.append(list)
            # list2.append(list_read_excel)
            # list1.append(list2)
            print(list_read_excel)
            # write(list1)