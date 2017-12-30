#要创建一个set，需要提供一个list作为输入集合
s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)	# 数学上的交集
print(s1 | s2)	# 数学上的并集