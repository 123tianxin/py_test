import requests, json
from bmob.constant import *


# 操作的bmob数据库表
url_file = "https://api.bmob.cn/2/files/"

# 链接bmob的权限申请
App_ID = getAppID()
Api_Key = getApiKey()
headers = { "X-Bmob-Application-Id": App_ID, 
            "X-Bmob-REST-API-Key": Api_Key, 
            "Content-Type": "text/plain"}

def uploadFile(fileName):
    files = {
        "file": open(fileName, "rb")
    }
    res = requests.post(url_file+fileName, headers=headers, files=files)
    temp = json.loads(res.text)
    return temp['url']

if __name__ == '__main__':
    uploadFile('tips.txt')