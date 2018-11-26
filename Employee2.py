class Employee:
    '员工类的基类'
    empCount = 0 # 员工人数

    # 初始化方法
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
   
    # 显示员工数
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    # 显示员工信息
    def displayEmployee(self):
        print ("Name : ", self.name,  ", Salary: ", self.salary)


emp1 = Employee("章三", 2000)
emp2 = Employee("李四", 5000)
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )


