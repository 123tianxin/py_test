import pickle

# 数据源
d = dict(name='敏敏', age=20)

with open('dump.txt', 'wb') as fw:
    pickle.dump(d, fw)
    fw.close()

with open('dump.txt', 'rb') as fr:
    d = pickle.load(fr)
    fr.close()

print(d)