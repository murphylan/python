class Parent:        # 定义父类
    parentAttr = 100
    def __init__(self):
        print ("调用父类的初始化方法")

    def parentMethod(self):
        print ('调用父类的方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print ("父类属性 :", Parent.parentAttr)

class Child(Parent): # 定义子类
    def __init__(self):
        print ("调用子类的初始化方法")

    def childMethod(self):
        print ('调用子类的方法')

c = Child()          # 子类实例
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类的方法
c.setAttr(200)       # 通过基类的方法设置属性值
c.getAttr()          # 通过基类的方法获取属性值



