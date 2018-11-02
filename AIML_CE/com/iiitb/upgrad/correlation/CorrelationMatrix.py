import pandas as pd
import matplotlib.pyplot as plt

#currencies = pd.read_csv("../../../../../currencies.csv")
#print(currencies.corr().to_csv("../..//../../../currencies_correlation.csv"))
#plt.matshow(currencies.corr())
#plt.show()
#print(currencies.corr(method="pearson"))
#print(currencies.corr(method="kendall"))
#print(currencies.corr(method="spearman"))

#cust_rating = pd.read_csv('https://query.data.world/s/ILc-P4llUraMaYN6N6Bdw7p6kUvHnj')
#col = cust_rating.loc[:, "rating":"service_rating"]
#cust_rating['avg_rating'] = round(col.mean(axis=1))
#round(cust_rating['avg_rating'])
#print(cust_rating)
#print(cust_rating.head(10))

#order = pd.read_csv('https://query.data.world/s/3hIAtsCE7vYkPEL-O5DyWJAeS5Af-7')
#order['Order_Date'] = pd.to_datetime(order['Order_Date'])
#order['day'] = pd.DatetimeIndex(order['Order_Date']).day
#print(order.head(10))

students = pd.read_csv("../../../../../grades.csv")
students['submit_time'] = pd.to_datetime(students['submit_time'])
students['day'] = pd.DatetimeIndex(students['submit_time']).day
students['date'] = pd.DatetimeIndex(students['submit_time']).date
students['month'] = pd.DatetimeIndex(students['submit_time']).month
students['year'] = pd.DatetimeIndex(students['submit_time']).year
students['hour'] = pd.DatetimeIndex(students['submit_time']).hour
students['minutes'] = pd.DatetimeIndex(students['submit_time']).minute
students['format of submission'] = students.submission.str[-3:]
students.to_csv("../../../../../detailed_grades.csv")

print(students.head(10))