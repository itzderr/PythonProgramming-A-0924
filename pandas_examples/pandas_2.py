import pandas as pd

dict = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

brics = pd.DataFrame(dict)
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# brics["name_length"] = brics["country"].apply(len)
for label, row in brics.iterrows():
    brics.loc[label, "name_length"] = len(row["country"])

print(brics)