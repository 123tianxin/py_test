fpath = 'fileDemo.txt'

with open(fpath, 'r', encoding="utf-8") as fr:
    str = fr.read()
    print("读操作：")
    print(str)


with open(fpath, 'a', encoding="utf-8") as fw:
    str = '写入操作处理;\n'
    fw.write(str)
    print("写操作：")
    print(str)