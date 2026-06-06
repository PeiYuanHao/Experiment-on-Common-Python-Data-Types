dic = {}

while True:
	s = input("请输入字符串：")
	if s == "":
		break
	for word in s.split():
		if word in dic:
			dic[word] = dic[word] + 1
		else:
			dic[word] = 1

for word in sorted(dic, key=dic.get, reverse=True):
	print(word, dic[word])

