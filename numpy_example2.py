import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

np_height = np.array(height)
np_weight = np.array(weight)

print(np_height > 1.75)
print(np_height[np_height > 1.75])

np_bmi = np_weight / np_height ** 2
print(np_bmi)

# print(type(height))
# print(type(np_height))
