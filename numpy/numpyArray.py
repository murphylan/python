#coding:utf-8

import numpy as np

#初始化a,使其变成3*8的矩阵
a=np.arange(24).reshape(3,8)
print(a)

#将多维数组变成1维数组
b=a.ravel()
# ravel 方法返回的是数组的视图
print("变成1维数组：",b)

#将多维数组变成1维数组，faltten 方法返回的是真实的数组，需要分配新的内存空间
b = b.flatten();
print("拉直之后：",b)

#改变 b 本身的数组,会改变所作用的数组
b.resize(2,12)

#不改变 b 本身的数组
c=b.reshape(2,12)
print(c)



