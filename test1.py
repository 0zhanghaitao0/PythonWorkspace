#以固定格式输出，点标记图，热力图
import xlrd
def read_excel():
    # 打开文件
    workBook = xlrd.open_workbook(r'E:\信令数据\tmp\20180827\part-00000_xx4.xlsx')
    # 1.获取sheet的名字
    # 1.1 获取所有sheet的名字(list类型)
    allSheetNames = workBook.sheet_names()
    #print(allSheetNames)
    # 1.2 按索引号获取sheet的名字（string类型）
    sheet1Name = workBook.sheet_names()[0]
    #print(sheet1Name)
    ## 2.2 法2：按sheet名字获取sheet内容
    sheet1_content2 = workBook.sheet_by_name('part-00000_xx4')
    # 3. sheet的名称，行数，列数
    #print(sheet1_content2.name, sheet1_content2.nrows, sheet1_content2.ncols)
    # 4. 获取整行和整列的值（数组）
    #rows = sheet1_content2.row_values(3)  # 获取第四行内容
    #cols = sheet1_content2.col_values(2)  # 获取第三列内容
    #print(rows)
    list=[]
    for  i in range(1,sheet1_content2.nrows):
        list1=[]
        list1.append(sheet1_content2.cell(i, 4).value)
        list1.append(sheet1_content2.cell(i, 3).value)
        list1.append(int(sheet1_content2.cell(i, 13).value)*2)
        # list1.append(int(sheet1_content2.cell(i, 5).value%1000000))
        #list1.append("circle")
        list.append(list1)

    #print(list)
    return list
def list_to_dict(list):#列表转换成指定格式
    list3=[]
    for list1 in list:
        #print(list1)
        lng = list1[1]
        lat = list1[0]
        count = list1[2]
        str_temp = '{"lng":' + str(lng) + ',"lat":' + str(lat) + ',"count":' + str(count) + '},'
        print(str_temp)


if __name__ == '__main__':
    list_read_excel = read_excel()
    list_dict = list_to_dict(list_read_excel)
    #format(list_read_excel)
    print(list_read_excel)
