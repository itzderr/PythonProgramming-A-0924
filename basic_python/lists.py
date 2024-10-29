# list: a sequence of elements of any data type
countries = ["Brazil", "Canada", "Colombia", "Ecuador", "France", "Iran", "Japan", "South Korea", "Taiwan", "USA", "Mexico", "Nepal"]

# indexing a list (index starts from 0)
print(countries[0])
print(countries[-1])  # last element
print(len(countries))  # the number of elements in the list

# slicing a list
# list[start:end]   start <=  < end
print(countries[:3])
print(countries[3:])

# assign a new element
countries[4] = "ABC"
print(countries)

# swap elements
first = countries[0]
countries[0] = countries[1]
countries[1] = first
print(countries)

# lists methods (functions)
languages = ["C", "C++", "Python", "Java", "JavaScript"]

# append(element): add a new element at the end of the list
# insert(index, element): add a new element at the given index
languages.append("SQL")
languages.insert(0, "Swift")
print(languages)

# pop(index)
# remove(element)
languages.pop(0)
languages.remove("JavaScript")
print(languages)

# index(element): returns the index of element in the list
print(languages.index("Python"))

# +: concatenate (combine)
# *: repeat num
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
print(nums1 + nums2)
print(nums1 * 3)

# 'nested' lists
students = [[1, "John", "Canada"], [2, "Max", "USA"], [3, "Peter", "UK"]]
inner = students[1]  # inner = [2, "Max", "USA"]
print(inner[2])
print(students[1][2])

# 'list comprehension' -> 'google'
