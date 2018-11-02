import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

sb.set_style("whitegrid")

df_market = pd.read_csv("../market_fact.csv")

# Histogram and Density Plot
#plt.figure(1)
#plt.subplot(121)
#sb.distplot(df_market['Shipping_Cost'])



#Rug Plot
#plt.subplot(122)
#sb.distplot(df_market['Shipping_Cost'][:1000], rug=True, hist=False)
sb.distplot(df_market['Sales'][:1000], rug=True, hist=False)


plt.show()

