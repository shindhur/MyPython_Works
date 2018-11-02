import pandas as pd
import seaborn as sb
import numpy as np

import matplotlib.pyplot as plt

countries_list = [
'Botswana',
'Cameroon',
'Ethiopia',
'Eritrea',
'The Gambia',
'Ghana',
'Kenya',
'Lesotho',
'Liberia',
'Malawi',
'Mauritius',
'Namibia',
'Nigeria',
'Rwanda',
'Seychelles',
'Sierra Leone',
'South Africa',
'South Sudan',
'Sudan',
'Swaziland',
'Tanzania',
'Uganda',
'Zambia',
'Zimbabwe',
'Antigua and Barbuda',
'The Bahamas',
'Barbados',
'Belize',
'Canada',
'Dominica',
'Grenada',
'Guyana',
'Jamaica',
'Saint Kitts and Nevis',
'Saint Lucia',
'Saint Vincent and the Grenadines',
'Trinidad and Tobago',
'United States','India',
'Pakistan',
'Philippines',
'Singapore','Australia',
'Fiji',
'Kiribati',
'Marshall Islands',
'Federated States of Micronesia',
'Nauru',
'New Zealand',
'Palau',
'Papua New Guinea',
'Samoa',
'Solomon Islands',
'Tonga',
'Tuvalu',
'Vanuatu','Ireland',
'Malta',
'United Kingdom']

df_companies = pd.read_csv("../../../../../Assignments/InvestmentAnalysis/companies.txt", encoding='unicode_escape', sep="\t");
print(df_companies.info())
print(df_companies.describe())
print("-------------------------------------------")
#df_companies.rename(columns={'permalink': 'company_permalink'}, inplace=True)
df_companies_nodups = df_companies.drop_duplicates(subset='permalink')
df_companies_nodups['permalink'] = df_companies_nodups['permalink'].str.lower()
#print(df_companies.head())
#print(df_companies_nodups.head())
#print("-------------------------------------------")
print(df_companies.info())
print(df_companies_nodups.info())
print("-------------------------------------------")
print(df_companies.describe())
print(df_companies_nodups.describe())
print("-------------------------------------------")
#print(df_companies.shape)
#print(df_companies_nodups.shape)
#print("-------------------------------------------")
print("----------------------------------------- End of Reading Companies File -----------------------------------------")

pd.options.display.float_format = '{:,.2f}'.format
df_rounds = pd.read_csv("../../../../../Assignments/InvestmentAnalysis/rounds2.csv", encoding='unicode_escape');

df_rounds_nodups  = pd.DataFrame(df_rounds['company_permalink'].drop_duplicates())
#df_rounds_nodups2 = pd.DataFrame(df_rounds.drop_duplicates(subset='company_permalink'))
df_rounds['company_permalink'] = df_rounds['company_permalink'].str.lower()
#print(df_rounds.head())
#print(df_rounds_nodups.head())
#print(df_rounds_nodups2.head())
#print("-------------------------------------------")
#print(df_rounds.info())
#print(df_rounds_nodups.info())
print(df_rounds.info())
print("-------------------------------------------")
#print(df_rounds.describe())
#print(df_rounds_nodups.describe())
print(df_rounds.describe())
print("-------------------------------------------")
#print(df_rounds.shape)
#print("-------------------------------------------")
print("----------------------------------------- End of Reading Rounds File -----------------------------------------")

print("----------------------------------------- Printing Companies and Rounds -----------------------------------------")
print(df_companies_nodups)
print(df_rounds)
print("----------------------------------------- Printed Companies and Rounds -----------------------------------------")

#df_company_rounds = df_companies.merge(df_rounds_nodups2, how="inner", on="company_permalink")
master_frame = pd.merge(df_companies_nodups, df_rounds, left_on="permalink", right_on="company_permalink", how="outer")
print(master_frame.info())
print("-------------------------------------------")
print(master_frame.describe())
print("-------------------------------------------")
#print(df_company_rounds.shape)
#print("-------------------------------------------")
#print(master_frame[['permalink','name','category_list','funding_round_type','funding_round_code','raised_amount_usd']])
#master_frame[['permalink','name','category_list','funding_round_type','funding_round_code','raised_amount_usd']].to_csv('master_data.csv', encoding='utf-8')

#master_df_frame = pd.DataFrame(master_frame[['permalink','name','category_list','funding_round_type','funding_round_code','raised_amount_usd']])
master_frame_grouped_df = master_frame.groupby(['funding_round_type'])
master_frame_fr_ra_df = pd.DataFrame(master_frame_grouped_df['raised_amount_usd'].mean().sort_values(ascending=False)).reset_index()

print("After Getting Mean --> master_frame_fr_ra_df --> Venture is Best")

print(master_frame_fr_ra_df)        # Needed for Plot 1
print(master_frame_fr_ra_df.info())

#plt.scatter(master_frame_fr_ra_df['raised_amount_usd'], master_frame_fr_ra_df['funding_round_type'])
#plt.xlabel('Raised Amount')
#plt.ylabel('Funding Round Type')
#plt.yscale('funding_round_type')
#plt.show()

#print(master_frame_fr_ra_df.describe())

#sb.distplot(master_frame_fr_ra_df['raised_amount_usd'][:1000], rug=True, hist=False)
#plt.show()



print(master_frame)
print("------------------------------ Master Frame -------------------------")
print(master_frame.info())
print("------------------------------ Master Frame Info-------------------------")

#master_df_country_frame = pd.DataFrame(master_frame[['permalink','country_code','funding_round_type','raised_amount_usd']])
venture_df = pd.DataFrame(master_frame.loc[master_frame['funding_round_type'] == 'venture'])
print(venture_df)
#print(master_df_country_frame)

#selected_venture = master_df_country_frame[(master_df_country_frame.funding_round_type == 'venture')]
print("---------------------------------Selected Venture----------------------------------")
print(venture_df.info())
print(venture_df.describe())
print("---------------------------------Printed Selected Venture----------------------------------")
selected_venture_grouped_df = venture_df.groupby(['country_code'])
print(selected_venture_grouped_df)
top9 = pd.DataFrame(selected_venture_grouped_df['raised_amount_usd'].sum().sort_values(ascending=False)).reset_index()
print(top9.head(9))


print(venture_df['category_list'])
venture_df['primary_sector'] = venture_df['category_list'].apply(lambda x : str(x).split('|')[0])
print(venture_df['primary_sector'])
print("---------------------------------Printed venture_df----------------------------------")

venture_dataFrame = pd.DataFrame(venture_df['primary_sector'])
print(venture_dataFrame.info())
print(venture_dataFrame.describe())

#venture_dataFrame_nodups = pd.DataFrame(venture_dataFrame['primary_sector'].drop_duplicates())
#print(venture_dataFrame_nodups)
#print(venture_dataFrame_nodups.info())
#print(venture_dataFrame_nodups.describe())

print("---------------------------------Printed Venture Data Frame ----------------------------------")

mapping_df = pd.read_csv("../../../../../Assignments/InvestmentAnalysis/mapping.csv", encoding='unicode_escape');

print(mapping_df)
print(mapping_df.describe())
print(mapping_df.info())
print('---------------------------------- Mapping Again ---------------------------')

final_mapping_df = pd.melt(mapping_df, id_vars=['category_list'], value_vars=['Automotive & Sports',	'Blanks',
                                                'Cleantech / Semiconductors',
                                                'Entertainment', 'Health',
                                                'Manufacturing',	'News, Search and Messaging',
                                                'Others',	'Social, Finance, Analytics, Advertising'])

final_mapping_df = final_mapping_df[final_mapping_df.value != 0]
final_mapping_df = final_mapping_df.rename(columns = {'variable':'main_sector'})
print(final_mapping_df)

print("---------------------------------Printing mapping_df----------------------------------")
#no_null_categories_mapping_series = mapping_df.drop(mapping_df.index[0])
print(final_mapping_df.describe())
print(final_mapping_df.info())



categories_list_frame = pd.merge(venture_df, final_mapping_df, left_on="primary_sector", right_on="category_list", how="inner")
#pd.DataFrame(categories_list_frame).to_csv('categories_list.csv',encoding='utf-8')

usa_dataframe = pd.DataFrame(categories_list_frame.loc[categories_list_frame['country_code'] == 'USA'])
gbr_dataframe = pd.DataFrame(categories_list_frame.loc[categories_list_frame['country_code'] == 'GBR'])
ind_dataframe = pd.DataFrame(categories_list_frame.loc[categories_list_frame['country_code'] == 'IND'])
#usa_dataframe.to_csv('usa_csv.csv',encoding='utf-8')
#print(usa_dataframe)
#print(usa_dataframe.info())
#print(usa_dataframe.describe())

usa_grouped_df = pd.DataFrame(usa_dataframe.groupby(['country_code','main_sector']).raised_amount_usd.agg(['count','sum']))
print(usa_grouped_df)

gbr_grouped_df = pd.DataFrame(gbr_dataframe.groupby(['country_code','main_sector']).raised_amount_usd.agg(['count','sum']))
print(usa_grouped_df)

ind_grouped_df = pd.DataFrame(ind_dataframe.groupby(['country_code','main_sector']).raised_amount_usd.agg(['count','sum']))
print(ind_grouped_df)

#usa_mainsector_df = pd.merge(usa_grouped_df, categories_list_frame, left_on="primary_sector", right_on="primary_sector", how="inner")
#print(usa_mainsector_df)
#usa_mainsector_df.to_csv('usa_mainsector_df.csv',encoding='utf-8')
#gbr_dataframe = pd.DataFrame(venture_df.loc[venture_df['country_code'] == 'GBR'])
#print(gbr_dataframe)

#ind_dataframe = pd.DataFrame(venture_df.loc[venture_df['country_code'] == 'IND'])
#print(ind_dataframe)

top_sector_countwise_company_usa = pd.DataFrame(usa_dataframe.loc[usa_dataframe['main_sector'] == 'Others'])
top_sector_countwise_company_usa = top_sector_countwise_company_usa[pd.notnull(top_sector_countwise_company_usa['raised_amount_usd'])]
top_sector_countwise_company_usa = top_sector_countwise_company_usa.sort_values('raised_amount_usd', ascending=False)
print(top_sector_countwise_company_usa[['name','country_code','primary_sector','main_sector','raised_amount_usd']])
top_sector_countwise_company_usa[['name','country_code','primary_sector','main_sector','raised_amount_usd']].to_csv('top_sector_countwise_company_usa.csv',encoding='utf-8')

top_sector_countwise_company_gbr = pd.DataFrame(gbr_dataframe.loc[gbr_dataframe['main_sector'] == 'Others'])
top_sector_countwise_company_gbr = top_sector_countwise_company_gbr[pd.notnull(top_sector_countwise_company_gbr['raised_amount_usd'])]
top_sector_countwise_company_gbr = top_sector_countwise_company_gbr.sort_values('raised_amount_usd', ascending=False)
print(top_sector_countwise_company_gbr[['name','country_code','primary_sector','main_sector','raised_amount_usd']])
top_sector_countwise_company_gbr[['name','country_code','primary_sector','main_sector','raised_amount_usd']].to_csv('top_sector_countwise_company_gbr.csv',encoding='utf-8')

top_sector_countwise_company_ind = pd.DataFrame(ind_dataframe.loc[ind_dataframe['main_sector'] == 'Others'])
top_sector_countwise_company_ind = top_sector_countwise_company_ind[pd.notnull(top_sector_countwise_company_ind['raised_amount_usd'])]
top_sector_countwise_company_ind = top_sector_countwise_company_ind.sort_values('raised_amount_usd', ascending=False)
print(top_sector_countwise_company_ind[['name','country_code','primary_sector','main_sector','raised_amount_usd']])
top_sector_countwise_company_ind[['name','country_code','primary_sector','main_sector','raised_amount_usd']].to_csv('top_sector_countwise_company_ind.csv',encoding='utf-8')

#----------------------------------------------------------------------------------------

#x1 = master_frame_fr_ra_df.at[6, 'raised_amount_usd']/master_frame_fr_ra_df['raised_amount_usd'].sum()*100

#list_fractionofinv = [master_frame_fr_ra_df.at[11, 'raised_amount_usd'], master_frame_fr_ra_df.at[3, 'raised_amount_usd']]
#print(master_frame_fr_ra_df.describe())
#print(master_frame_fr_ra_df)




#plt.xlabel("Top 9 Sectors")
#plt.ylabel("Count")
#sb.barplot(x='main_sector', y=pd.DataFrame(usa_dataframe.groupby(['country_code','main_sector']).raised_amount_usd.agg(['count'])), data=usa_dataframe)
usa_grouped_plot = pd.DataFrame(usa_dataframe.groupby(['country_code','main_sector']).raised_amount_usd.agg(['count'])).sort_values('count', ascending=False)
print(usa_grouped_plot)

gbr_grouped_plot = pd.DataFrame(gbr_dataframe.groupby(['country_code','main_sector']).raised_amount_usd.agg(['count'])).sort_values('count', ascending=False)
print(gbr_grouped_plot)

ind_grouped_plot = pd.DataFrame(ind_dataframe.groupby(['country_code','main_sector']).raised_amount_usd.agg(['count'])).sort_values('count', ascending=False)
print(ind_grouped_plot)

#sb.jointplot('main_sector', 'count', usa_grouped_plot)
#plt.show()
#-----------------------------------3rd Plot ------------------------------------------------------
sb.catplot(y="main_sector", hue="country_code",data=usa_dataframe, kind="count",height=4,  aspect=.7);
plt.show()


#------------------------------------ 1st Plot ---------------------------
master_frame_fr_ra_df['percentage'] = master_frame_fr_ra_df['raised_amount_usd']/master_frame_fr_ra_df['raised_amount_usd'].sum()*100
print(master_frame_fr_ra_df)
print("-------------------- Almost There---------------------")
#master_frame_fr_ra_df['funding_round_type'] = master_frame_fr_ra_df.index
master_frame_fr_ra_df = master_frame_fr_ra_df.set_index(['funding_round_type'])
#print(master_frame_fr_ra_df.loc['seed'])
master_frame_fr_ra_df = master_frame_fr_ra_df.loc[master_frame_fr_ra_df.index.isin(['private_equity','seed','venture'])]
#print(master_frame_fr_ra_df.loc[master_frame_fr_ra_df.index.isin(['private_equity','seed','venture'])])
#print(master_frame_fr_ra_df.loc[master_frame_fr_ra_df['funding_round_type'].isin(['seed','venture'])])
#print("-------------------- There---------------------")
#print(master_frame_fr_ra_df.loc[master_frame_fr_ra_df['funding_round_type'].isin(['venture','private_equity'])])
print(master_frame_fr_ra_df.info())
print(master_frame_fr_ra_df.reset_index())
#master_frame_fr_ra_df = master_frame_fr_ra_df.loc['venture']
plt.figure(figsize=(12, 6))
plt.subplot(1,2,1)
sb.barplot(x='percentage', y='funding_round_type', data=master_frame_fr_ra_df.reset_index())

plt.subplot(1,2,2)
sb.barplot(x='raised_amount_usd',y='funding_round_type', data=master_frame_fr_ra_df.reset_index(), estimator=np.mean)
plt.show()

#------------------------------------- 2nd Plot -------------------------------------
plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
sb.barplot(x='country_code', y='raised_amount_usd', data=top9.head(9))
plt.xlabel("Top 9 Countries")
plt.ylabel("Total Amount of Investment")
plt.show()

