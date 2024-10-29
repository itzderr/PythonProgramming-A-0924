# 'procedural' programming
# - instructions step by step (line by line)
# - 'functions'

# 'object-oriented' programming
# - data science 50/50
# - 'class' -> object
# creating a class -> 'blueprint'
# there are lots of rules
# "custom data type"
# "group of functions and variables"

# why?
# - organize your code
# - reusability
# - scalability / flexibility

class Car:
    # class variable
    # python_uses_snake_case
    # javascriptUsesCamelCase
    car_count = 0

    # initializer (constructor): special function to create an object
    def __init__(self, make, model, price):
        # instance(object) variables
        self.make = make
        self.model = model
        self.price = price

    @classmethod
    def increment_car_count(cls):
        cls.car_count += 1

    def drive(self):
        print(f"Driving {self.make} {self.model}")

    def stop(self):
        print(f"Stopping {self.make} {self.model}")


