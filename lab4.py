# Exercise 1
students = {
    "Alice": [85, 78, 92],
    "Bob": [79, 74, 81],
    "Charlie": [91, 82, 85],
    "David": [76, 85, 83],
    "Eve": [88, 79, 92]
}

# task 1
alice = students["Alice"]
total_score = sum(alice)
n = len(alice)
print(total_score / n)
