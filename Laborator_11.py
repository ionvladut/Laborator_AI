# EX 1

import pandas as pd


df = pd.read_csv('StudentsPerformance.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(df.head(5))
print(df.info())
print(df.describe())
print(df.isnull().sum())

# EX 2

num_var = df.select_dtypes(include="number").columns
print("Variabilele numerice sunt: " + str(list(num_var)))
cat_var = df.select_dtypes(exclude="number").columns
print("Variabilele categorice sunt: " + str(list(cat_var)))

# EX 3

df[num_var] = df[num_var].fillna(df[num_var].median())
df[cat_var] = df[cat_var].fillna("Unknown")
print(df.isnull().sum())
print(df)

# EX 4

