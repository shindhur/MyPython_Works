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

df1 = pd.merge(df_market, df_orders_dimen, how="inner", on="Ord_id")
df1.Order_Date = pd.to_datetime(df1.Order_Date)

time_df = df1.groupby('Order_Date')['Sales'].sum()
print(time_df.head())
print(type(time_df.head()))

plt.figure(figsize=(16, 8))
sb.tsplot(data=time_df)
plt.show()

df1['month'] = df1['Order_Date'].dt.month
df1['year'] = df1['Order_Date'].dt.year
print(df1.head())

df_time = df1.groupby(['year','month']).Sales.mean()
print(df_time.head())
plt.figure(figsize=(8, 6))
sb.tsplot(df_time)
plt.xlabel("Time")
plt.ylabel("Sales")
plt.show()

#---------------------------------------------------------

print("Month-Month  Insights")

year_month = pd.pivot_table(df1, values='Sales', index='year', columns='month', aggfunc='mean')
print(year_month.head())
plt.figure(figsize=(12, 8))
sb.heatmap(year_month, cmap='YlGnBu')
plt.show()