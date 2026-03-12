import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv')
print(df.head())
print(df.shape)
print(df.isnull().sum())
df["country"] = df["country"].fillna("Unknown")
df["director"] = df["director"].fillna("Unknown")
print(df.isnull().sum())

print(df["type"].value_counts())
df["type"].value_counts().plot(kind="bar")
plt.title("Netflix İçerik Türleri")
plt.xlabel("Tür")
plt.ylabel("Sayı")
plt.show()

print(df["country"].value_counts().head(10))
print(df["release_year"].value_counts().sort_index())

df["release_year"].value_counts().sort_index().plot(kind="line")
plt.title("Netflix İçeriklerinin Yıllara Göre Dağılımı")
plt.xlabel("Yıl")
plt.ylabel("Sayı")
plt.show()

df["duration"] = df["duration"].str.replace(" min", "").str.replace(" Season", "").str.replace(" Seasons", "")
df["duration"] = pd.to_numeric(df["duration"], errors="coerce")

print(df.sort_values("duration", ascending=False)[["title","duration"]].head())
print(df["director"].value_counts().head(10))
print(df["listed_in"].value_counts().head(10))