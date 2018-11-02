import pandas as pd

marks = pd.read_csv('https://query.data.world/s/HqjNNadqEnwSq1qnoV_JqyRJkc7o6O')
#print(marks.info())
#print(marks.describe())
#print(marks.isna().sum())
#print(marks.isnull().sum())
#print(marks[marks.isnull().any(axis=1)])
print("----------------------------------------------------")
print(marks.isnull().sum())
marks = marks.dropna(thresh=2)
print(marks)
print(marks.isnull().sum())

customer = pd.read_csv('https://query.data.world/s/y9rxL9mGdP6AXPiDaIL4yYm6DsfTV2')

customer['Cust_id'] = customer.Cust_id.str.slice(5, 6)
print(customer.head(10))

#--------------------------------

#sleepstudy['Reaction'] = sleepstudy.round({'Reaction': 1})     // Rounding off Data
#print(sleepstudy.head(10))

#-------------- Drop Duplicates --------------------
rating = pd.read_csv('https://query.data.world/s/EX0EpmqwfA2UYGz1Xtd_zi4R0dQpog')

rating_update = rating.drop_duplicates(subset=None, keep='first', inplace=False)

print(rating.shape)
print(rating_update.shape)