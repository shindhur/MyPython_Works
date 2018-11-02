# Series and Dataframes in Pandas

import numpy as np
import pandas as pd

# Series
a = pd.Series([2,6,4,9,21])
print("-------------------------------------------")
print(a)
print("-------------------------------------------")
s = a.apply(lambda x: x**2)
print(s)
print("-------------------------------------------")
# Dataframe
df = pd.DataFrame(
    {'name': ['Shindhur', 'Moneca', 'Rokalla', 'Mallidi'],
                   'age': [31, 27, 13, 72],
                   'occupation': ['Developer', 'Marine', 'Electrical', 'Designer']
                   }
                  )
#print(df)

df1 = pd.read_csv("../market_fact.csv")
print("-------------------------------------------")
print(df1.head())
print("-------------------------------------------")
print(df1.tail())
print("-------------------------------------------")
print(df1.info())
print("-------------------------------------------")
print(df1.describe())
print("-------------------------------------------")
print(df1.shape)
print("-------------------------------------------")
print(df1.columns)
print("-------------------------------------------")
print(df1.set_index("Ord_id").head())
print("-------------------------------------------")
df_2 = df1.sort_values(by=["Prod_id", "Sales"])
print(df_2.head(20))
print("-------------------------------------------")
print("Row Selection")
print(df1[2:7])
print("-------------------------------------------")
print("This pulls every alternate row")
print(df1[2::2].head())
print(type(df1[2::2].head()))
print("-------------------------------------------")
print()
print(df1['Sales'].head())
print(df1.Sales.head())
print('Type of DF in case of Columns is')
print(type(df1.Sales.head()))
print('----------------------------------------')
print('Pulling Multiple Columns')
print(df1[['Sales', 'Discount']].head())
print(type(df1[['Sales', 'Discount']].head()))

#---------------------------------------------------------------------
##### Position Based and Label Based Access of Elements in DF
#---------------------------------------------------------------------
# Using Positions ----------------------------------------------------
#help(pd.DataFrame.iloc)
print(df1.iloc[2, 4])   #Row 3, Column 4
print(df1.iloc[5])  #Row 6
print(df1.iloc[5, :])   #Same as Above
print(df1.iloc[[3, 7, 8]])  # Multiple Rows
print(df1.iloc[4:8])  # Range of Rows

print((df1.iloc[:, 4]).head()) #Entire Column 5
print((df1.iloc[:, 2:4]).head()) #Range of Columns
print((df1.iloc[:, [2, 4]]).head()) #Multiple Columns
print(df1.iloc[[3, 5], [2, 4]]) #3rd row and 5th row and columns 3 and 5
print(df1.iloc[3:5, 2:4])

# Using Labels ---------------------------------------------------------
print(df1.loc[2, 'Sales'])

df1.set_index('Ord_id', inplace=True)
print(df1.loc[['Ord_5446', 'Ord_5406'], :].head())
print(df1.loc[['Ord_5446', 'Ord_5406'], 'Sales':'Profit'].head())

#------------------------------------------------
#Subset of Dataset based on condition

print(df1.Sales>3000)   #Column values where Sales value is > 3000
print((df1.loc[df1.Sales > 3000, :]).head())
print((df1.loc[df1['Sales'] > 3000, :]).head())