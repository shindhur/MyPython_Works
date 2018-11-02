import pandas as pd
import seaborn as sb
import numpy as np

import matplotlib.pyplot as plt

pd.options.display.float_format = '{:,.2f}'.format

def lowercase(args):
  if isinstance(args, str):
      return args.lower()

print("Performing Data Cleanup On Companies Data")
df_companies = pd.read_csv("../../../../../Assignments/InvestmentAnalysis/companies.txt", encoding='unicode_escape', sep="\t");
df_companies = df_companies.drop_duplicates(subset='permalink')
df_companies['permalink'] = df_companies['permalink'].str.lower()

round(100*(df_companies.isnull().sum()/len(df_companies.index)), 2)
df_companies['country_code'].isnull().sum()
df_companies = df_companies[~pd.isnull(df_companies['country_code'])]
df_companies.isnull().sum()

df_companies.loc[pd.isnull(df_companies['category_list']), ['category_list']] = 'Others'
df_companies.isnull().sum()

print("Performing Data Cleanup On Rounds Data")
df_rounds = pd.read_csv("../../../../../Assignments/InvestmentAnalysis/rounds2.csv", encoding='unicode_escape');
df_rounds['company_permalink'] = df_rounds['company_permalink'].str.lower()
df_rounds.loc[pd.isnull(df_rounds['raised_amount_usd']), ['raised_amount_usd']] = df_rounds['raised_amount_usd'].mean()

#Table 1.1 How many unique companies are present in rounds2?
df_rounds_unique_companies = df_rounds['company_permalink'].unique();
print(df_rounds_unique_companies.size)

#Table 1.1 How many unique companies are present in companies?
df_companies_unique_companies = df_companies['permalink'].unique();
print(df_companies_unique_companies.size)

#Table 1.1 Any companies in the rounds2 file which are not present in companies??
unique_companies_in_rounds = pd.Series(df_rounds['company_permalink'].isin(df_companies['permalink']))

#Table 1.1 How many observations are present in master_frame?
master_frame = pd.merge(df_companies, df_rounds, left_on="permalink", right_on="company_permalink", how="outer")
print(master_frame.shape)
print("--------------------------------- End of Table 1 -------------------------------------")


print("Performing Data Manipulation by replacing Null Raised Amount USD values with Mean and Cleaning up Null funding_round_type rows")
master_frame.loc[pd.isnull(master_frame['raised_amount_usd']), ['raised_amount_usd']] = master_frame['raised_amount_usd'].mean()
master_frame = master_frame[~pd.isnull(master_frame['funding_round_type'])]
master_frame.isnull().sum()

#Table 2.1 Most representative value of the investment amount for each of the four funding types (venture, angel, seed, and private equity)
master_frame_grouped_df = master_frame.groupby(['funding_round_type'])
master_frame_repvalue_df = pd.DataFrame(master_frame_grouped_df['raised_amount_usd'].mean().sort_values(ascending=False)).reset_index()

#Table 2.2 Based on the most representative investment amount calculated above, which investment type do you think is the most suitable for Spark Funds ?
print("After Getting Mean --> Venture is Best")
print("--------------------------------- End of Table 2 -------------------------------------")


print(master_frame_repvalue_df)        # Needed for Plot 1
print(master_frame_repvalue_df.info())

venture_df = pd.DataFrame(master_frame.loc[master_frame['funding_round_type'] == 'venture'])
print(venture_df)

selected_venture_grouped_df = venture_df.groupby(['country_code'])
#Spark Funds wants to see the top nine countries which have received the highest total funding
top9 = pd.DataFrame(selected_venture_grouped_df['raised_amount_usd'].sum().sort_values(ascending=False)).reset_index()

#For the chosen investment type, make a data frame named top9 with the top nine countries
print(top9.head(9))


print(venture_df['category_list'])

#Extract the primary sector of each category list from the category_list column
venture_df['primary_sector'] = venture_df['category_list'].apply(lambda x : str(x).split('|')[0])
venture_df['primary_sector'] = venture_df['primary_sector'].apply(lambda x: lowercase(x))


mapping_df = pd.read_csv("../../../../../Assignments/InvestmentAnalysis/mapping.csv", encoding='unicode_escape');
mapping_df['category_list'] = mapping_df['category_list'].apply(lambda x: lowercase(x))
melted_mapping_df = pd.melt(mapping_df, id_vars=['category_list'], value_vars=['Automotive & Sports',	'Blanks',
                                                'Cleantech / Semiconductors',
                                                'Entertainment', 'Health',
                                                'Manufacturing',	'News, Search and Messaging',
                                                'Others',	'Social, Finance, Analytics, Advertising'])

melted_mapping_df = melted_mapping_df[melted_mapping_df.value != 0]
melted_mapping_df = melted_mapping_df.rename(columns = {'variable':'main_sector'})

# Map each primary sector to one of the eight main sectors
categories_list_frame = pd.merge(venture_df, melted_mapping_df, left_on="primary_sector", right_on="category_list", how="inner")

#Create three separate data frames D1, D2 and D3 for each of the three countries containing the observations of funding type FT falling within the 5-15 million USD range
usa_dataframe = pd.DataFrame(categories_list_frame.loc[categories_list_frame['country_code'] == 'USA'])
gbr_dataframe = pd.DataFrame(categories_list_frame.loc[categories_list_frame['country_code'] == 'GBR'])
ind_dataframe = pd.DataFrame(categories_list_frame.loc[categories_list_frame['country_code'] == 'IND'])

usa_grouped_df = pd.DataFrame(usa_dataframe.groupby(['country_code','main_sector']).raised_amount_usd.agg(['count','sum']))
print(usa_grouped_df)
print(usa_grouped_df['count'].sum())
print(usa_grouped_df['sum'].sum())

gbr_grouped_df = pd.DataFrame(gbr_dataframe.groupby(['country_code','main_sector']).raised_amount_usd.agg(['count','sum']))
print(gbr_grouped_df)
print(gbr_grouped_df['count'].sum())
print(gbr_grouped_df['sum'].sum())

ind_grouped_df = pd.DataFrame(ind_dataframe.groupby(['country_code','main_sector']).raised_amount_usd.agg(['count','sum']))
print(ind_grouped_df)
print(ind_grouped_df['count'].sum())
print(ind_grouped_df['sum'].sum())

# For the top sector count-wise (point 3), which company received the highest investment
top_sector_countwise_company_usa = pd.DataFrame(usa_dataframe.loc[usa_dataframe['main_sector'] == 'Others'])
top_sector_countwise_company_usa = top_sector_countwise_company_usa[pd.notnull(top_sector_countwise_company_usa['raised_amount_usd'])]
top_sector_countwise_company_usa = top_sector_countwise_company_usa.sort_values('raised_amount_usd', ascending=False)
print(top_sector_countwise_company_usa)

top_sector_countwise_company_gbr = pd.DataFrame(gbr_dataframe.loc[gbr_dataframe['main_sector'] == 'Others'])
top_sector_countwise_company_gbr = top_sector_countwise_company_gbr[pd.notnull(top_sector_countwise_company_gbr['raised_amount_usd'])]
top_sector_countwise_company_gbr = top_sector_countwise_company_gbr.sort_values('raised_amount_usd', ascending=False)
print(top_sector_countwise_company_gbr)

top_sector_countwise_company_ind = pd.DataFrame(ind_dataframe.loc[ind_dataframe['main_sector'] == 'Others'])
top_sector_countwise_company_ind = top_sector_countwise_company_ind[pd.notnull(top_sector_countwise_company_ind['raised_amount_usd'])]
top_sector_countwise_company_ind = top_sector_countwise_company_ind.sort_values('raised_amount_usd', ascending=False)
print(top_sector_countwise_company_ind)

#For the second-best sector count-wise (point 4), which company received the highest investment?
print(pd.DataFrame(usa_dataframe.loc[usa_dataframe['main_sector'] == 'Cleantech / Semiconductors']).sort_values(by="raised_amount_usd",ascending=False))
print(pd.DataFrame(gbr_dataframe.loc[gbr_dataframe['main_sector'] == 'Cleantech / Semiconductors']).sort_values(by="raised_amount_usd",ascending=False))
print(pd.DataFrame(ind_dataframe.loc[ind_dataframe['main_sector'] == 'News, Search and Messaging']).sort_values(by="raised_amount_usd",ascending=False))

#usa_grouped_plot = pd.DataFrame(usa_dataframe.groupby(['country_code','main_sector']).raised_amount_usd.agg(['count'])).sort_values('count', ascending=False)
#print(usa_grouped_plot)

#gbr_grouped_plot = pd.DataFrame(gbr_dataframe.groupby(['country_code','main_sector']).raised_amount_usd.agg(['count'])).sort_values('count', ascending=False)
#print(gbr_grouped_plot)

#ind_grouped_plot = pd.DataFrame(ind_dataframe.groupby(['country_code','main_sector']).raised_amount_usd.agg(['count'])).sort_values('count', ascending=False)
#print(ind_grouped_plot)

#------------------------------------ 1st Plot ---------------------------
master_frame_repvalue_df['percentage'] = master_frame_repvalue_df['raised_amount_usd']/master_frame_repvalue_df['raised_amount_usd'].sum()*100
master_frame_repvalue_df = master_frame_repvalue_df.set_index(['funding_round_type'])
master_frame_repvalue_df = master_frame_repvalue_df.loc[master_frame_repvalue_df.index.isin(['private_equity','seed','venture'])]

plt.figure(figsize=(12, 12))
plt.subplot(1, 2, 1)
sb.barplot(x='percentage', y='funding_round_type', data=master_frame_repvalue_df.reset_index())
plt.title("Percentage Investment by Fund Type")

plt.subplot(1, 2, 2)
sb.barplot(x='raised_amount_usd',y='funding_round_type', data=master_frame_repvalue_df.reset_index(), estimator=np.mean)
plt.title("Average Investment by Fund Type")
plt.show()

#------------------------------------- 2nd Plot -------------------------------------
plt.figure(figsize=(10, 10))
sb.barplot(x='raised_amount_usd', y='country_code', data=top9.head(9))
plt.xlabel("Total Amount of Investment")
plt.ylabel("Top 9 Countries")
plt.show()

#-----------------------------------3rd Plot ------------------------------------------------------
usa_top3Sector = usa_dataframe.query('main_sector == ["Others", "Cleantech / Semiconductors","Social, Finance, Analytics, Advertising"]')
sb.catplot(y="main_sector", hue="country_code",data=usa_top3Sector,col="country_code",col_wrap=4 ,kind="count",height=2,aspect=2)

gbr_top3Sector = gbr_dataframe.query('main_sector == ["Others", "Cleantech / Semiconductors","Social, Finance, Analytics, Advertising"]')
sb.catplot(y="main_sector", hue="country_code",data=gbr_top3Sector,col="country_code",col_wrap=4 , kind="count",height=2,aspect=2)

ind_top3Sector = ind_dataframe.query('main_sector == ["Others", "News, Search and Messaging","Social, Finance, Analytics, Advertising"]')
sb.catplot(y="main_sector", hue="country_code",data=ind_top3Sector,col="country_code",col_wrap=4 , kind="count",height=2,aspect=2)

plt.show()