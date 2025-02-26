import pandas as pd

# serie = pd.Series([10,20,20])
# #print(serie)

# df = pd.DataFrame({
#     'Nom': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25,30,35],
#     'Ville': ['Lille', 'Lille', 'Tourcoing']
# })

# print(df[df['Age'] > 28])

# df['Salaire'] = [10000,20000,30000]
# print(df)

# print(df.groupby('Ville')['Age'].mean())

df = pd.read_csv("Salaries.csv", sep=',')

# print(df.head(20))

# print(df.tail(10))

# print(df.size)

# print(df.columns)

# print(df.dtypes)

result = df.groupby('sex')[['salary']].mean()
print(df.groupby('sex')[['salary']].mean())


