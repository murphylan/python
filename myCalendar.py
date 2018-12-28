# 导入日历 module.
import calendar

cal = calendar.month(2019, 1)
print("2019年1月份日历:")
print(cal)

# cal = calendar.monthcalendar(2019,1)
# print (cal)


cal = calendar.monthrange(2019, 1)

print(cal)
