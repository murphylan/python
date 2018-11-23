def changeme( mylist ):
    "改变传入的List对象值"
    print ("打印改变前的原始值: ", mylist)
   
    mylist[2]=50
    print ("打印改变后的新值: ", mylist)
    return


mylist = [10,20,30]
changeme( mylist )
print ("观察调用时的值，发现已经改变了: ", mylist)

