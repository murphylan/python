# 打开文件
fo = open("demo.txt", "r+")
str = fo.read(10)
print ("读取的字符串 : ", str)

# 检查当前的位置
position = fo.tell()
print ("当前的位置 : ", position)

# 再次在开头重新定位指针
position = fo.seek(0, 0)
# 为了区别起见，我们设置不同的位置
str = fo.read(20)
print ("再次读取的字符串 : ", str)

# 关闭文件
fo.close()



