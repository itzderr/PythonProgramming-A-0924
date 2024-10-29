# 1.
l = [1, 2, 3, 4, 5]
print(l[2])

# 2.
l.append(6)
print(l)

l.pop(1)
print(l)

# 3
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(nums[:5])
print(nums[-3:])
print(nums[::2])

# 4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(numbers))
print(max(numbers))
print(min(numbers))

# 5. [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([i ** 2 for i in range(1, 11)])

# 6.
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_list[1][1])

# 1
s = "Hello, World!"
print(s[0], s[-1])

# 2
s1 = "Python Programming"
print(s1[:6])
print(s1[7:])

# 3
s2 = "hello, world!"
print(s2.upper())
print(s.replace("World", "Python"))

# 4
print("Hello" + " " + "World")

# 5
fruits = "apple,banana,cherry"
fruits_list = fruits.split(",")
print(fruits_list)

# 6
name = "Justin"
age = "30"
print(f"My name is {name} and I am {age} years old")

# 7
word = input("Enter a word: ")
print(word[::-1])  # reverse a string/list
if word == word[::-1]:
    print("It is a palindrome")
else:
    print("It's not a palindrome")

# 8
chars = ['P', 'y', 't', 'h', 'o', 'n']
print("".join(chars))