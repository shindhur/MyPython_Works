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

df1 = pd.merge(df_market, df_cust_dimen, how="inner", on="Cust_id")
df2 = pd.merge(df1, df_prod_dimen, how="inner", on="Prod_id")
df3 = pd.merge(df2, df_shipping_dimen, how="inner", on="Ship_id")
main_df = pd.merge(df3, df_orders_dimen, how="inner", on="Ord_id")

plt.figure(figsize=(12, 6))

#Default statistics in Mean
plt.subplot(1, 2, 1)
sb.barplot(x='Product_Category', y='Sales', data=main_df)
plt.title("Mean Sales")

plt.subplot(1, 2, 2)
sb.barplot(x='Product_Category', y='Sales', data=main_df, estimator=np.median)
plt.title("Median Sales")
plt.show()

#-------------------------------------------------------------------------------

plt.figure(figsize=(12, 8), num=None, dpi=80, facecolor='w', edgecolor='k')
sb.barplot(x='Customer_Segment', y='Profit', hue='Product_Category', data=main_df, estimator=np.median)
plt.show()

#-------------------------------------------------------------------------------

plt.figure(figsize=(10, 10))
sb.barplot(x='Profit', y='Product_Sub_Category', hue='Product_Category', data=main_df, estimator=np.median)
plt.show()