import pandas as pd
from selenium import webdriver
import time


url = 'http://api.map.baidu.com/staticimage/v2?'

#配置url
def get_url(latlng):
    ak = 'vKHOVd6Gd0ZECdBgwuOcSCaTvX67bD3G'
    url2 = url + 'ak=' + ak + '&width=600' + '&height=400' + '&center=' + '江苏省南京市水务局' + '&markers=%s&zoom=12&markerStyles=s,A,0xff0000' % latlng +'&zoom=15'
    return url2

#从excel表格中读取经纬度
data = pd.read_excel(r'E:\信令数据\tmp\20180807\aaa.xlsx')

#创建一个列表用于存放经纬度
list=[]

#读出列表中的每行经纬度
def get_lat_lng(i):
    #print(data)
    data = pd.read_excel(r'E:\信令数据\tmp\20180807\aaa.xlsx')
    row= data.iloc[i,:].to_list()
    coords = str(row[3])+','+str(row[4])
    return coords

#循环读出经纬度并存放于列表中
for indexs in data.index:
    lat_lng=get_lat_lng(indexs)
    list.append(lat_lng)

#用‘|’合并列表中的经纬度
str1='|'
latlng = str1.join(list)

#获取完整URL
url3 = get_url(latlng)
print(url3)

#模拟谷歌浏览器打开
path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)
browser.get(url3)
time.sleep(120)
browser.quit()





