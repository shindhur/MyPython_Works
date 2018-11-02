import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_market = pd.read_csv("../market_fact.csv")

plt.boxplot(df_market['Order_Quantity'])
plt.show()
print(df_market['Order_Quantity'].describe())
print(df_market['Sales'].describe())
plt.figure(1)

plt.subplot(121)
plt.boxplot(df_market['Sales'])

plt.subplot(122)
plt.boxplot(df_market['Sales'])
plt.yscale('log')
plt.show()

#---------------------------------------------------------

print("-----------------Histogram------------------------")

plt.hist(df_market['Sales'])
plt.yscale('log')
plt.show()

plt.scatter(df_market['Sales'], df_market['Profit'])
plt.show()
