import pandas as pd
import numpy as np

df = pd.read_csv("../melbourne.csv")
print("-------------------------------------------")
print(df.isnull().sum())
print("-------------------------------------------")
print(df.isnull().any())
print("-------------------------------------------")
print(df.isnull().any(axis=0))
print("-------------------------------------------")
print(df.isnull().any(axis=1))
print("-------------------------------------------")

df = pd.read_csv("../market_fact.csv")
print(round(100*(df.isnull().sum()/len(df.index)), 2))
print("-------------------------------------------")
print("*******************************************")

df_melbourne = pd.read_csv("../melbourne.csv")
df1 = df_melbourne[df_melbourne.isnull().sum(axis=1)<=5]
print(round(100*(df1.isnull().sum()/len(df1.index)), 2))
print("*************Ignored Rows which have more than 5 missing items************")

print(df.loc[:, 'Product_Base_Margin'].describe())
df.loc[np.isnan(df['Product_Base_Margin']), ['Product_Base_Margin']] = df['Product_Base_Margin'].mean()
print(round(100*(df.isnull().sum()/len(df.index)), 2))