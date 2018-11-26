class Employee:
    '所有员工的基类'
    empCount = 0 #员工人数

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
   
    def displayCount(self):
        print ("员工人数 %d" % Employee.empCount)

    def displayEmployee(self):
        print ("姓名 : ", self.name,  ", 工资: ", self.salary)


# 下面将创建Employee类的第一个实例
emp1 = Employee("章三", 2000)
# 下面将创建Employee类的第二个实例
emp2 = Employee("李四", 5000)


emp1.displayEmployee()
emp2.displayEmployee()
# 打印员工总数
print ("员工总数 %d" % Employee.empCount)


emp1.salary = 7000  # 将员工章三的工资更新为7000.
emp1.name = '张三'  # 接着修改他的姓名.
# del emp1.salary  # 删除他的工资.


hasattr(emp1, 'salary')    # 如果emp1实例中存在属性‘salary’，返回true
getattr(emp1, 'salary')    # 返回emp1实例中属性‘salary’的值
setattr(emp1, 'salary', 7000) # 设置emp1实例中属性‘salary’的值为7000
delattr(emp1, 'salary')    # 删除emp1实例中的属性‘salary’

