
countries = ["Canada", "China", "USA", "France", "UK"]

# go by index
for i in range(len(countries)):
    print(i)

# go by element
for country in countries:
    print(country)

# both
for i, country in enumerate(countries):
    print(f"{i}: {country}")


# numpy array nditer
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

l = np.array([arr1, arr2])
for i in np.nditer(l):
    print(i)