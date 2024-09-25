# string: "a sequence of characters"
#  'sequence' - order
#  strings are immutable (unchangeable)

# index:0123456789012
name = "Justin Bieber"

# 1. Indexing a string
print(name[6])
print(name[0])
print(name[-1])  # last character
print(name[-2])  # second last character

# len(): returns the length of a string
print(len(name))
print(name[len(name) - 1])  # last character

# 2. Slicing a string
# str[start:end]   start <=  < end
print(name[0:3])
print(name[7:13])
print(name[7:len(name)])
print(name[7:])  # always till the end
print(name[:6])  # always start from 0

# (example)
actor = "Ryan Reynolds"
# slice last name
print(actor[5:])

# * multiply a string by an integer : repeat
print(actor * 3)
# + adding another string : concatenate (combine)
print(actor + " from Vancouver")

# string methods (functions)
address = "816 Granville ST, Vancouver, BC"

# 1. uppercase / lowercase / capitalize
print(address.upper())
print(address.lower())
print(address.capitalize())

# 2. find() returns -1 if not found
#    index() throws an error if not found
print(address.find("vancouver"))
# print(address.index("vancouver"))

# 3. isdigit(), isalpha(), isalnum(), etc
user_id = "a1924b3"
if user_id.isdigit():
    print("Valid User ID")
elif user_id.isalpha() or user_id.isalnum():
    print("Invalid User ID: use numbers only")

# 4. split() - splits a string into a list of substrings
#    join() - joins a list of strings into one big string
#    strip() - strip out all white spaces (space, tab, newline)
l = address.split(",")
street_address = l[0]
city = l[1].strip()
province = l[2].strip()

full_message = f"I live in {street_address}, {city}, {province}."
print(full_message)

cities = ["Vancouver", "Burnaby", "Richmond", "West Vancouver", "North Vancouver", "Surrey", "Coquitlam"]
print(",".join(cities))

