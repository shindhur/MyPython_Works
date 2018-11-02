import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df_market = pd.read_csv("../market_fact.csv")
df_market = df_market[(df_market.Profit < 10000) & (df_market.Profit > 0) & (df_market.Sales < 20000)]
sb.jointplot('Sales', 'Profit', df_market)
plt.show()

#------------------------------------------------------------------------------------------------------

btc = pd.read_csv("../crypto_data/bitcoin_price.csv")
eth = pd.read_csv("../crypto_data/ethereum_price.csv")
ltc = pd.read_csv("../crypto_data/litecoin_price.csv")
mon = pd.read_csv("../crypto_data/monero_price.csv")
neo = pd.read_csv("../crypto_data/neo_price.csv")
qtm = pd.read_csv("../crypto_data/qtum_price.csv")
rpl = pd.read_csv("../crypto_data/ripple_price.csv")

btc.columns = btc.columns.map(lambda x: str(x) + '_BTC')
eth.columns = eth.columns.map(lambda x: str(x) + '_BTC')
ltc.columns = ltc.columns.map(lambda x: str(x) + '_BTC')
mon.columns = mon.columns.map(lambda x: str(x) + '_BTC')
neo.columns = neo.columns.map(lambda x: str(x) + '_BTC')
qtm.columns = qtm.columns.map(lambda x: str(x) + '_BTC')
rpl.columns = rpl.columns.map(lambda x: str(x) + '_RPL')

print(btc.head())