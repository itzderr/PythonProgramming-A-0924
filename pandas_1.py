import pandas as pd
#
# dict = {
#     "country": ["Brazil", "Russia", "India", "China", "South Africa"],
#     "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
#     "area": [8.516, 17.10, 3.286, 9.597, 1.221],
#     "population": [200.4, 143.5, 1252, 1357, 52.98]
# }
#
# brics = pd.DataFrame(dict)
# brics.index = ["BR", "RU", "IN", "CH", "SA"]
# print(brics.loc["RU"])
# print(brics)
#
movies = pd.read_csv("movies.csv")
print(movies)

# column access [column]
# print(movies["title"])  # Series
print(movies[["title", "release_year"]])  # DataFrame

# row access []
print(movies[1:6])

# loc
print(movies.loc[1])  # Series
print(movies.loc[[0, 1, 5]])  # DataFrame

# row & col loc
print(movies.loc[[0, 1, 5], ["title", "release_year"]])

# entire row & col (title, release_year)
print(movies.loc[:, ["title", "release_year"]])
print(movies.loc[[0, 1, 2], :])

# iloc
print(movies.iloc[[1]])
print(movies.iloc[:, [1]])

