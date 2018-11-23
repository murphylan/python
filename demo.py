def printinfo( age, *vartuple ):
    "打印传入的参数"
    print ("年龄: ", age)

    for var in vartuple:
          print (var)

    return

# 调用函数
printinfo( 30 )
# 调用函数
printinfo( 70, 60, 50, 40 )




