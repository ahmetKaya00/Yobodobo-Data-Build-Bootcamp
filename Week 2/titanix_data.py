import pandas as pd

df = pd.read_csv('titanic.csv')

print(df.head())

print(df.info())

print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df["Age"].isnull().sum())

print(df["Survived"].value_counts())

print(df[df["Sex"] == "female"]["Survived"].mean())
print(df[df["Sex"] == "male"]["Survived"].mean())
print(df.groupby("Age")["Survived"].mean())
print(df["Fare"].mean())

print(df.sort_values("Fare", ascending=False).head())