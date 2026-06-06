s = input("请输入一个字符串：")

flag = True
i = 0
j = len(s) - 1

while i < j:
	if s[i] != s[j]:
		flag = False
		break
	i = i + 1
	j = j - 1

if flag:
	print("是对称字符串")
else:
	print("不是对称字符串")

