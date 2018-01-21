import requests, sys
from tools.parseHTML import *
from tools.builtTempFile import *
from bmob.do_bmob import *
from bmob.do_bmob_file import *


# 要请求的地址链接
change_url = "http://blog.wutnews.net"

# 存储请求超时的param
paramList = []

def subThread(params):
    try:
        res = requests.get(url = change_url, params={'p': params}, timeout=15)
        status_code = res.status_code
        if(status_code == 200):
            print("查询成功!", params)
            reduceHTML = initHTML(res.text)
        
            isFull = isFullText(reduceHTML)
            if(isFull == True):
                reduceHTML = initHTML(res.text)

                PID = str(params)
                date = getDate(reduceHTML)
                author = getAuthor(reduceHTML)
                author_url = getAuthorURL(reduceHTML)
                title = getTitle(reduceHTML)

                # 解析博客内容
                content = getContent(reduceHTML)
        
                # 生成临时存储文件
                fileName = PID + '.txt'
                tempFile(fileName, content)

                # 上传到bmob，并返回文件存储链接
                file_url = uploadFile(fileName)

                # 删除临时文件
                deleteTempFile(fileName)

                # 构建一条数据
                dataLine = builtData(PID, date, author, author_url, title, file_url)
                saveLine(dataLine)

        else:
            print("该链接不存在", status_code, params)
    except requests.exceptions.ConnectionError as e:
        print("请求超时...", "--> params: ", params)
        global paramList
        paramList.append(params)
    except requests.exceptions.ReadTimeout as e:
        print("请求超时...", "--> params: ", params)
        paramList.append(params)


# 存储因为请求超时，而无法执行的request
def getParamList():
    global paramList
    tempList = paramList
    paramList = []
    return tempList