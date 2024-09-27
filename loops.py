# loops
# - for loop
# for 'loop_var' in 'collection':
#
# collection(iterable): range(start, end, steps), string, list
#     iterate(repeat)
# loop_var: to assign each value in a collection

for i in range(5):  # (0, 1, 2, 3, 4)
    print(f"{i}: Hello")

for i in range(2, 7):  # (2, 3, 4, 5, 6)
    print(f"{i}: Hi")

for i in range(1, 10, 2):  # (1, 3, 5, 7, 9)
    print(f"{i}: 2 steps each")

for i in range(10, 1, -1):
    print(f"{i}: negative step")


# iterating a string
city = "Vancouver"

# count the number of vowels?
vowel_count = 0
for ch in city:
    if ch in "AEIOUaeiou":
        vowel_count += 1  # vowel_count = vowel_count + 1

print(f"{city} has {vowel_count} vowels.")

# iterating a list
nums = [1, 40, 20, 14, 35, 31, 7, 11]

# count the number of even numbers in the list
even_count = 0
for num in nums:
    if num % 2 == 0:
        even_count += 1

print(f"{nums} list has {even_count} even numbers.")


# - while loop
x = 0
while x < 5:
    print("Hello")
    x += 1

# count the number of vowels
city = "Vancouver"

i = 0
vowels = 0
while i < len(city):
    if city[i] in "AEIOUaeiou":  # check if a character is vowel
        vowels += 1
    i += 1

print(f"{city} has {vowels} vowels.")


nums = [1, 40, 20, 14, 35, 31, 7, 11]
# count the number of even numbers
j = 0
even = 0
while j < len(nums):
    if nums[j] % 2 == 0:
        even += 1
    j += 1

print(f"{nums} list has {even} even numbers.")


while True:  # infinite loop
    command = input("Enter 'q' to quit: ")
    if command == "q":
        print("Bye!")
        break  # stop
    elif command == 's':
        continue  # skip the rest

    print("Try again!")
