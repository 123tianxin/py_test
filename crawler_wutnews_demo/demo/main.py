import requests, sys
from tools.parseHTML import *
from tools.builtTempFile import *
from bmob.do_bmob import *
from bmob.do_bmob_file import *



# 要请求的地址链接
change_url = "http://blog.wutnews.net"
# 地址传递的参数，需要修改
params = 100
# 设置循环遍历的次数
cycle_times = 100

while cycle_times != 0:
    cycle_times = cycle_times -1

    res = requests.get(url = change_url, params={'p': params-cycle_times})
    status_code = res.status_code
    if(status_code == 200):
        print("查询成功!", params-cycle_times)
        reduceHTML = initHTML(res.text)
        
        isFull = isFullText(reduceHTML)
        if(isFull != True):
            continue
        else:
            reduceHTML = initHTML(res.text)

            PID = str(params-cycle_times)
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
        print("该链接不存在", status_code, params-cycle_times)
    
