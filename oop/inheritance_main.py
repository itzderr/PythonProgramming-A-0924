from oop.employee import Employee, Developer, Manager

e1 = Employee(3, "Aidan", 75000)
m1 = Manager(2, "Dan", 82000, "IT")
# m1.work()
d1 = Developer(1, "Josh", 80000, "Python")
# d1.work()

# inheritance
employees = [e1, m1, d1]
for employee in employees:
    employee.work()  # polymorphism - same type, different behaviour (method)
