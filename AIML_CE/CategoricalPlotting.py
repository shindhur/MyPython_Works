import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

sb.set(style="white")

df_market = pd.read_csv("../market_fact.csv")
df_cust_dimen = pd.read_csv("../cust_dimen.csv")
df_orders_dimen = pd.read_csv("../orders_dimen.csv")
df_prod_dimen = pd.read_csv("../prod_dimen.csv")
df_shipping_dimen = pd.read_csv("../shipping_dimen.csv")

#sb.boxplot(y=df_market['Sales'])
#plt.yscale('log')
#plt.show()

df = pd.merge(df_market, df_prod_dimen, how='inner', on='Prod_id')
df.head()

sb.boxplot(x='Product_Category', y='Sales', data=df)
plt.yscale('log')
plt.show()

df = df[(df.Profit < 1000) & (df.Profit > -1000)]
sb.boxplot(x='Product_Category', y='Profit', data=df)
plt.show()

#-------------------------------------------------------------

df1 = pd.merge(df_market, df_cust_dimen, how="inner", on="Cust_id")
df2 = pd.merge(df1, df_prod_dimen, how="inner", on="Prod_id")
df3 = pd.merge(df2, df_shipping_dimen, how="inner", on="Ship_id")
main_df = pd.merge(df3, df_orders_dimen, how="inner", on="Ord_id")
main_df = main_df[(main_df.Profit < 1000) & (main_df.Profit > -1000)]
sb.boxplot(x='Customer_Segment', y='Profit', data=main_df)

plt.show()

#---------------- 2 Categorical Variables -------------

plt.figure(num=None, figsize=(12, 8), dpi=80, facecolor='w', edgecolor='k')
sb.boxplot(x='Customer_Segment', y='Profit', hue='Product_Category', data=main_df)
plt.show()