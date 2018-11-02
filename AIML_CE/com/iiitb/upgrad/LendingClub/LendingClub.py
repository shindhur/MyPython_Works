import pandas as pd
import numpy as np

loan_df = pd.read_csv("../../../../../loan.csv", dtype={'next_pymnt_d': str}, sep=",", encoding='unicode_escape', low_memory=False)
print(loan_df.describe())
print(loan_df.info())
print(loan_df.isna().sum())

print("loan_df is the actual Data Frame")
print("Dropping columns with all values as NAN/Null ----> loan_noNulls_df")
loan_noNulls_df = loan_df.dropna(axis=1, how='all');
loan_noNulls_df = loan_noNulls_df.drop(['initial_list_status'], axis=1)
loan_noNulls_df = loan_noNulls_df.drop(['collections_12_mths_ex_med'], axis=1)
loan_noNulls_df = loan_noNulls_df.drop(['policy_code'], axis=1)
loan_noNulls_df = loan_noNulls_df.drop(['application_type'], axis=1)
loan_noNulls_df = loan_noNulls_df.drop(['acc_now_delinq'], axis=1)
loan_noNulls_df = loan_noNulls_df.drop(['chargeoff_within_12_mths'], axis=1)
loan_noNulls_df = loan_noNulls_df.drop(['delinq_amnt'], axis=1)
loan_noNulls_df = loan_noNulls_df.drop(['tax_liens'], axis=1)
loan_noNulls_df = loan_noNulls_df.drop(['desc'], axis=1)
loan_noNulls_df = loan_noNulls_df.drop(['pymnt_plan'], axis=1)
loan_noNulls_df = loan_noNulls_df.drop(['url'], axis=1)

#convert string values to numerical values
#int_rate and revol_util have '%', remove them and converting to float
loan_noNulls_df["int_rate"] = pd.Series(loan_noNulls_df["int_rate"]).str.replace("%", "").astype(float)
loan_noNulls_df["revol_util"] = pd.Series(loan_noNulls_df["revol_util"]).str.replace("%", "").astype(float)

#replace months with empty
loan_noNulls_df["term"] = loan_noNulls_df["term"].apply(lambda x: str(x).replace(' months',''))
loan_noNulls_df["term"].astype(int)

print("Checking Nulls is any for entire column")
print(loan_noNulls_df.isnull().sum())
loan_noNulls_df = loan_noNulls_df.drop_duplicates(keep='first',inplace=False)

loan_noNulls_df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

print(loan_noNulls_df.info())

print("Check Uniqueness of Loan Member ID's")
print("Unique Loan Count  ----> ")
print(len(loan_noNulls_df['id'].unique()))
print("More than 1 Loan For Same Member ----> ")
print(len(loan_noNulls_df['member_id'].unique()))

# Delete rows, columns: Rows could be deleted if the number of missing values are insignificant in number, as this would not impact the analysis. Columns could be removed if the missing values are quite significant in number.
# Splitting Month Year Columns into Multiple Columns
loan_noNulls_df_split = loan_noNulls_df["issue_d"].str.split("-", n = 1, expand = True)
loan_noNulls_df["issue_month"] = loan_noNulls_df_split[0]
loan_noNulls_df["issue_year"] = loan_noNulls_df_split[1]

loan_noNulls_df_split = loan_noNulls_df["last_pymnt_d"].str.split("-", n = 1, expand = True)
loan_noNulls_df["last_pymnt_d_month"] = loan_noNulls_df_split[0]
loan_noNulls_df["last_pymnt_d_year"] = loan_noNulls_df_split[1]


loan_noNulls_df = loan_noNulls_df[np.abs(loan_noNulls_df.annual_inc-loan_noNulls_df.annual_inc.mean()) <= (3*loan_noNulls_df.annual_inc.std())]
loan_noNulls_df = loan_noNulls_df[~(np.abs(loan_noNulls_df.annual_inc-loan_noNulls_df.annual_inc.mean()) > (3*loan_noNulls_df.annual_inc.std()))]
print(loan_noNulls_df.annual_inc.mean())

loan_noNulls_df.to_csv("../../../../../loan_noNulls.csv")

