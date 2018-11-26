class Student:
    __secretCount = 0  # 双下划线前缀定义的变量
  
    def count(self):
        self.__secretCount += 1
        print (self.__secretCount)

counter = Student()
counter.count()
counter.count()
# print (counter.__secretCount) # 访问类中的双下划线前缀定义的变量
print (counter._Student__secretCount)
print (str(counter))


