# 打开文件
fo = open("demo.txt", "r+")
str = fo.read(50)
print ("读取的字符串 : ", str)

# 关闭文件
fo.close()


