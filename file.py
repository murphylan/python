# 打开一个文件
fo = open("demo.py", "wb")
print ("显示文件名: ", fo.name)
print ("文件是否关闭 : ", fo.closed)
print ("打开文件的模式 : ", fo.mode)
fo.close()


