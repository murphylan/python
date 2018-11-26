a = 40      # 创建变量 <40>
b = a       # 创建引用. count  of <40> 
c = [b]     # 创建引用. count  of <40> 

del a       # 删除引用. count  of <40>
b = 100     # 删除引用. count  of <40> 
c[0] = -1   # 删除引用. count  of <40> 


class A:        # 定义类A
.....

class B:         # 定义类B
.....

class C(A, B):   # 子类C，同时继承类A和类B
.....


