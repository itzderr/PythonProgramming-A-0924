from oop.car import Car

marcelo = Car("Ferrari", "Spider 448", 400000)
Car.increment_car_count()
shigeo = Car("Lamborghini", "Hurricane", 450000)
Car.increment_car_count()

print(Car.car_count)  # class variable

marcelo.drive()
marcelo.stop()

shigeo.drive()
shigeo.stop()

print(type(marcelo))
print(type("hello"))
