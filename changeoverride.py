def changeme( mylist ):
    "传入List对象，我们将覆盖它的值"
    mylist = [1,2,3,4] # 我们将覆盖它的值
    print ("打印覆盖后传入的引用变量: ", mylist)
    return


mylist = [10,20,30]
changeme( mylist )
print ("观察这个变量的值: ", mylist)
