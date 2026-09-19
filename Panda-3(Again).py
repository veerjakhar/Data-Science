import pandas as pd

dfs = pd.read_csv("Panda-3(Sheet1).csv")

print(dfs)

abv60 = dfs[dfs["Passanger-age"] > 60]
print(abv60, "Are the passangers on board above 60")

avb12sus = dfs[(dfs["Passanger-age"] < 12)&(dfs["Survived"] == 1)]
print(avb12sus, "Are the people under 12 that survived")

avgage = dfs["Passanger-age"].mean()
print(avgage, "Is the average age")





ruafem = dfs[(dfs["Gender"] == "Female")&(dfs["Class"] == "1st")]
print(ruafem)

ruamale = dfs[(dfs["Gender"] == "Male")&(dfs["Class"] == "3rd")&(dfs["Survived"] == 1)]
print(ruamale, "These many people survived as a male in the 3rd class, Accurate rIGHT?")



avgfair = dfs.groupby("Class")["Fare"].mean()
print(avgfair, ": The ammont of class people that survived")

avgfair4 = dfs.groupby("Class")["Fare"] == 1
print(avgfair4)