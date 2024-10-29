import pandas as pd

dogs = pd.read_csv("dogs.csv")  # dataframe

# print(dogs.head())
# print(dogs.info())
# print(dogs.shape)
# print(dogs.describe())
# print(dogs.values)
# print(dogs.columns)
# print(dogs.index)

print(dogs)

# ascending (increasing order)
# descending (decreasing order)
# dogs = dogs.sort_values("Weight", ascending=False)
# dogs = dogs.sort_values(["Weight", "Height"])
# print(dogs["Name"])

# print(dogs[dogs["Height"] > 50])
# is_labrador = dogs["Breed"] == "Labrador"
# is_brown = dogs["Color"] == "Brown"
# print(dogs[(is_labrador) & (is_brown)])
# print(dogs[dogs["Color"].isin(["Black", "Brown"])])

dogs["Height_m"] = dogs["Height"] / 100
dogs["bmi"] = dogs["Weight"] / dogs["Height_m"] ** 2

print(dogs["bmi"].max())
# display dogs 'name', 'height in cm', 'bmi'
# where their bmi is less than 100
# order by height in descending order
# print(dogs[dogs["bmi"] < 100].sort_values("Height")[["Name", "Height", "bmi"]])

def pct30(col):
    return col.quantile(0.3)


def pct70(col):
    return col.quantile(0.7)


print(dogs["Weight"].agg([pct30, pct70]))

print(dogs)
print(dogs["Breed"].value_counts(sort=True, normalize=True))

is_black = dogs["Color"] == "Black"
black_dogs = dogs[is_black]
print(black_dogs["Weight"].mean())

print(dogs.groupby("Color")["Weight"].mean())

import numpy as np
# print(dogs.groupby(["Color", "Breed"])[["Weight", "Height"]].agg([max, min, sum, np.mean, np.prod]))


print(dogs.pivot_table(values="Weight", index="Color", columns="Breed", fill_value=0, margins=True))




















