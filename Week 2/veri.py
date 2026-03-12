import pandas as pd

data = {
    'isim': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'yas': [25, 30, 35, 40, 45],
    'sehir': ['Chicago', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'maas': [50000, 60000, 70000, 80000, 90000]
}
df = pd.DataFrame(data)
print(df)

print(df.shape)

print(df.columns)

print(df[['maas', 'sehir', 'yas']])

print(df[df['yas'] > 30])

print(df["maas"].mean())

print(df.groupby('sehir')['maas'].mean())

df["yillik_maas"] = df["maas"] * 12
print(df)

print(df.sort_values("maas", ascending=False))

data = {
    'isim': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'yas': [25, None, 35, 40, None],    
    'maas': [50000, 60000, None, 80000, 90000]
}
asdasdas
df = pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.isnull().sum())

df_filled = df.fillna({'yas': df['yas'].mean(), 'maas': df['maas'].mean()}) 
print(df_filled)


