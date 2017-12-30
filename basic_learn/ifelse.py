birth = input("输入你的出生年份：")
birth = int(birth)

if birth >= 2000:
	print("你是00后的孩纸！")
elif birth >= 1990:
	print("你是90后佛系青年人！")
else:
	print("你是中年或晚年危机啦！")