# tuple: a comma separated values (immutable)
# how to create a tuple
student1 = (1, "John", "Canada", "Canada")
employee1 = (312, "John", "Smith", "131-323-3213", "abc@gmail.com", 170, 60)
employee2 = (32, "Johnny", "Smith", "131-323-6713", "abcd@gmail.com", 175, 65)

employees = [employee1, employee2]

empl1 = employees[0]
print(empl1[1] + " " + empl1[2])

# student1[1] = "Justin" (not allowed)

# extract values from tuple separate variable
_, name, country, _ = student1
print(name, country)

# access elements using [index]
print(student1[1])

# tuple methods (functions)
print(student1.index("Canada"))
print(student1.count("Canada"))

# for single element tuple (add a comma at the end)
a = ("hello",)  # or "hello",
print(type(a))