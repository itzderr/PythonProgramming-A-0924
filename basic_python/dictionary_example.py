contacts_name   = ["John", "Patrick", "Vincent"]
contacts_number = ["778-253-4343", "236-239-2143", "604-131-5243"]

# dictionary in python: a set of key-value pairs, no order, no duplicate keys
# using dictionary:
contacts = {"John": "778-253-4343", "Patrick": "236-239-2143", "Vincent": "604-131-5243"}

# how to access the value using key
print(contacts["Patrick"])

# how to add a new key-value pair
contacts["Justin"] = "123-134-1435"
print(contacts)

# how to delete a key-value pair
del contacts["Vincent"]
print(contacts)

# how to update the value in dictionary
if "John" in contacts:  # to check if "John" exists in dictionary
    contacts["John"] = "000-000-0000"

print(contacts)

# How to get the sum of total population?
world_pop = {"Canada": 40, "USA": 300, "Brazil": 220,
             "Mexico": 127, "Japan": 125, "Colombia": 51,
             "South Korea": 51, "Taiwan": 20, "Ecuador": 18,
             "Iran": 89}

# iterating key value as a pair
total = 0
for k, v in world_pop.items():
    total += v
    print(f"{k}: {v}")

print(total)

# iterating values only
for v in world_pop.values():
    print(v)

# iterating keys only
for k in world_pop.keys():
    print(k)


# use _ when you don't use the loop variable
total1 = 0
for _, v in world_pop.items():
    total1 += v

for _ in range(5):
    print("Hello")


print(type(world_pop.keys()))
print(list(world_pop.keys()))  # convert dict_keys -> list

