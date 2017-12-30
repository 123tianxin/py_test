#辨识python中两种集合
#list是一种有序的集合，可以随时添加和删除其中的元素。
L_01 = ['Java', 'Python', 'Ruby', 'PHP']
print(len(L_01))
L_01.insert(4, "C++")
print(L_01.pop(4))
print(L_01[3])
L_01[3] = "javascript"
print(L_01[3])

#tuple和list非常类似，但是tuple一旦初始化就不能修改
T_01 = ('Apple', 'Google', 'Microsoft')
T_02 = ('a', 'b', ['A', 'B'])

print(T_01)
print(T_02)
