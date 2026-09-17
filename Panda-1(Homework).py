import pandas as pd

df = pd.DataFrame({
    "Name": ["Veer", "Rishab", "Khushi", "Youli", "Reya", "James"],
    "Math": [100.6, 98.7, 100, 100.3, 95.9, 80.8],
    "Science": [92.6, 96, 93.6, 94.7, 89.8, 90.4],
    "ELA": [96.8, 97.5, 95.1, 94.8, 93.9, 97.3]
})

print(df)

df["Average"] = df[["Math", "Science", "ELA"]].mean(axis = 1)

print(df[["Name", "Average"]])

abv95 = df[(df["Math"] >= 100)]

print(abv95)

print(df["Math"].max())
print(df["Science"].max())
print(df["ELA"].max())
