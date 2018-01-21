import re, os

# 在本目录下生成一个临时文件
# 用于存储博客内容
# 文件命名根据PID【例：PID.txt】
def tempFile(fileName, content):
    content = "<p>" + content
    with open(fileName, 'w', encoding='utf-8') as fw:
        temp = re.split('<p>(.*?)</p>', content)
        for line in temp:
            fw.write(line)
        fw.close()

# 删除临时文件
def deleteTempFile(fileName):
    os.remove(fileName)