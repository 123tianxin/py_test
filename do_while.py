# 计算1+2+3+...+100: 过滤掉10
sum = 0
n = 0
while n < 100:
    n = n + 1
    if n == 10:
        continue
    sum = sum + n
print(sum)

# 计算1x2x3x...x100:
acc = 1
n = 1
while n <= 100:
    acc = acc * n
    n = n + 1
    if n == 10:
    	break # break语句会结束当前循环
print(acc)