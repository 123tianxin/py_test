import requests, json
from bmob.constant import *

# 操作的bmob数据库表
url_form = "https://api.bmob.cn/1/classes/wutnews_datas"

# 链接bmob的权限申请
App_ID = getAppID()
Api_Key = getApiKey()
headers = {"X-Bmob-Application-Id": App_ID, 
            "X-Bmob-REST-API-Key": Api_Key, 
            "Content-Type": "application/json"}

# 构建数据结构
def builtData(PID='', date='', author='', author_url='', title='', file_url=''):
    datas = {   'PID': PID,
                'entry_date': date, 
                'author': author,
                'author_url': author_url,
                'entry_title': title,
                'file_url': file_url
            }
    return datas

# 获取所有的数据
def getAllLines():
    res = requests.get(url=url_form, headers=headers)
    
    temp = json.loads(res.text)
    return temp['results']

# 存储一行数据
def saveLine(data={"author": "demo"}):
    res = requests.post(url=url_form, headers=headers, data=json.dumps(data))


if __name__ == '__main__':
    results = getAllLines()
    for temp in results:
        print(temp)
    
    saveLine()
