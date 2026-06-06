a = input("请输入一串数字（用空格分隔）: ").split()

a = [int(x) for x in a]
b = list(set(a))

print("原列表: {}".format(a))
print("去重后: {}".format(b))