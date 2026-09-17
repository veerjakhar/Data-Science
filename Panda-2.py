import pandas as pd

df = pd.DataFrame({
    "City": ["San-Fransico", "Paris", "Floptropica", "Dubai","New Dehli", "Singapore"],
    "Avg Temp": [78, 79, 100, 92, 89, 74],
    "Humidity": [68, 83, 100, 94, 94, 76],
    "Rainfall-(in)": [14, 16, 100, 6, 32, 19]
})

# maxtemp = df["Avg Temp"].max()
# print(df[df["Avg Temp"] == maxtemp])
print(df.loc[df["Avg Temp"].idxmax(), "City"])

dfs = df["Rainfall-(in)"].mean()

print(dfs)
