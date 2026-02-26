# Create an Employee class.
#
# Employee should have:
#
# name
#
# salary
#
# And one action (method):
#
# 👉 show_details()
#
# Which should print:
#
# Employee name: Amit
# Salary: 50000

class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def showdetails(self):
        print(self.name,self.salary)

emp1 = employee("kanak",10000)

print(emp1.showdetails())