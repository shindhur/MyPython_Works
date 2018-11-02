import pandas as pd
import numpy as np

df_market = pd.read_csv("../market_fact.csv")
df_cust_dimen = pd.read_csv("../cust_dimen.csv")
df_orders_dimen = pd.read_csv("../orders_dimen.csv")
df_prod_dimen = pd.read_csv("../prod_dimen.csv")
df_shipping_dimen = pd.read_csv("../shipping_dimen.csv")
#-------------- Merging Dataframes------------Adding more Columns-----
df = pd.merge(df_market, df_cust_dimen, how="inner", on="Cust_id")
print(df.head())

#-------------- Concatinating Dataframes------------Adding more Rows-----
# Time consuming, so commented
#df_1 = pd.read_csv('https://query.data.world/s/vv3snq28bp0TJq2ggCdxGOghEQKPZo')
#df_2 = pd.read_csv('https://query.data.world/s/9wVKjNT0yiRc3YbVJaiI8a6HGl2d74')
#df_3 = pd.concat([df_1, df_2], axis=0, sort=False)
#print(df_3.head())

#------------------ Grouping and Summarising ----------------------------
df1 = pd.merge(df_market, df_cust_dimen, how="inner", on="Cust_id")
df2 = pd.merge(df1, df_prod_dimen, how="inner", on="Prod_id")
df3 = pd.merge(df2, df_shipping_dimen, how="inner", on="Ship_id")
main_df = pd.merge(df3, df_orders_dimen, how="inner", on="Ord_id")
print("Merged all DF's ---------------------------------------------------")
print(main_df.head())
print("Merged all DF's ---------------------------------------------------")

cust_grouped_df = main_df.groupby('Customer_Segment')
print(cust_grouped_df['Profit'].sum().sort_values(ascending=False))
print(pd.DataFrame(cust_grouped_df['Profit'].sum().sort_values(ascending=False)))

product_grouped_df = main_df.groupby('Product_Category')
product_grouped_df = main_df.groupby(['Product_Category', 'Product_Sub_Category'])
print(pd.DataFrame(product_grouped_df['Profit'].mean().sort_values(ascending=False)))


df_forest = pd.read_csv("../forestfires.csv")
df_1 = df_forest.groupby(['month', 'day'])['rain', 'wind'].mean()
print(df_1.head(20))

#---------------------------------------------------------------------------------

print("Adding New Column")
df_market['is_profitable'] = df_market['Profit'].apply(lambda x:x>0)
print(df_market.head())
print("---------------------------------------------------------------------------")

#--------------------------------------------------------------- Pivot Table--------------

print(main_df.pivot_table(values="Sales", index="Customer_Segment", aggfunc="mean"))

df_forest = pd.read_csv("../forestfires.csv")
df_1 = df_forest.pivot_table(index=['month', 'day'], values=['rain', 'wind'], aggfunc='mean')
print(df_1.head(20))