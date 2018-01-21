import re

def match_Str(str, resHTML):
    try:
        temp = re.search(str, resHTML, re.S)
        temp = temp.groups()
        temp = temp[0]
        return temp
    except AttributeError as e:
        print("my --> AttributeError: 'NoneType' object has no attribute 'groups'")
    except TypeError as e:
        print("my --> TypeError: 'NoneType' object is not subscriptable")
    finally:
        return None
    

# 初始化HTML，压缩不会用到的部分
def initHTML(resHTML):
    temp = match_Str('<article(.*?)</article>', resHTML)
    return temp

# 做个判断，是否是完整的一篇文章
def isFullText(resHTML):
    try:
        temp = re.search('>阅读全文</a>', resHTML, re.S)
        if(temp == None):
            return True
    except Exception as e:
        print("my --> TypeError: expected string or bytes-like object")
    finally:
        return False
    

# 获取博客发表时间
def getDate(resHTML):
    resHTML = match_Str('<span class="entry-date">(.*?)</span>', resHTML)
    temp = match_Str('>(.*?)</a>', resHTML)
    return temp

# 获取博客作者的姓名
def getAuthor(resHTML):
    resHTML = match_Str('<span class="author vcard">(.*?)</span>', resHTML)
    temp = match_Str('>(.*?)</a>', resHTML)
    return temp

# 获取博客作者链接
def getAuthorURL(resHTML):
    resHTML = match_Str('<span class="author vcard">(.*?)</span>', resHTML)
    temp = match_Str('href="(.*?)"', resHTML)
    return temp

# 获取博客文章标题
def getTitle(resHTML):
    temp = match_Str('class="entry-title">(.*?)</h', resHTML)
    return temp

# 获取博客内容
def getContent(resHTML):
    # temp = match_Str('<div class="entry-content">(.*?)<div', resHTML)
    temp = match_Str('<p>(.*?)<div', resHTML)
    return temp

if __name__ == '__main__':
    getDate()

