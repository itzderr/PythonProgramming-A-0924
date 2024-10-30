# object-oriented programming
# functional programming
# new data types
# - Employee
# - Developer, Manager

class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working.")


# when your creating Developer object, you need to first create your Employee object (super/parent class)
class Developer(Employee):
    def __init__(self, id, name, salary, prog_lang):
        super().__init__(id, name, salary)  # call super(Employee) class's initializer
        self.prog_lang = prog_lang

    # overriding a method
    def work(self):
        print(f"Developer {self.name} is working!")


class Manager(Employee):
    def __init__(self, id, name, salary, department):
        super().__init__(id, name, salary)  # call super(Employee) class's initializer
        self.department = department

