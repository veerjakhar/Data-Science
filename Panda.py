import pandas as pd

df = pd.DataFrame({
    "Name": ["Diya", "Rishab"], 
    "Age": [13, 12], 
    "City": ["MountainHouse", "Milpitas"],
    "Ethnicity": ["Indian", "Indian"]
    })

print(df.head())
print(df.shape)
print(df["Age"].max())
print(type(df["Age"]))
print(df["Age"].shape)
print(df.info())
# print(df.dtypes())

print(df.describe())

dfs = pd.read_csv("Book1.csv")

print(dfs.head())
print(dfs.info())
#print(df.dtypes())

NameAndAge = dfs[["Name", "Relationship"]]

print(NameAndAge.head())
print(NameAndAge.shape)

Above12 = dfs[dfs["Age"] > 12]
print(Above12.head())
print(Above12.shape)

age9and12 = dfs[(dfs["Age"] == 9)|(dfs["Age"] == 12)]

print(age9and12)