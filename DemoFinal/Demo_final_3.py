import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.linear_model import LinearRegression
from scipy.stats import linregress

sales_data = pd.read_excel("sales_data.xlsx")

df = DataFrame(sales_data.iloc[:5])
print(df)

for i in range(len(df)):
    print(f"total sales of {df['Product'].iloc[i]} is => {df['Quantity'].iloc[i] * df['Price'][i]}")

df['Total Sales'] = df['Quantity'] * df['Price']

plt.bar(df['Product'], df['Total Sales'])
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.title("Total Sales for Each Product")
# plt.show()

X = df['Price']
y = df['Quantity']

slope, intercept, r_value, p_value, std_err = linregress(X, y)

print(f"Regression coefficient: {slope}; \nintercept: {intercept}")

mean_of_quantity = np.mean(df['Quantity'])
std_of_quantity = np.std(df['Quantity'])

percentile_25_of_price = np.percentile(df['Price'], 75)
percentile_75_of_price = np.percentile(df['Price'], 75)

new_df = pd.DataFrame({'Product': df['Product'], 'Total Sales': df['Total Sales']})
print(f"new dataframe: {new_df}")

new_df.to_excel("sales_summary.xlsx", index=False)

np.random.seed(42)
daily_sales = np.random.randint(50, 200, size=100)

print(f"daily sales: {daily_sales}")

sales_data['Daily Sales'] = daily_sales

quantity_array = sales_data['Quantity'].to_numpy()
price_array = sales_data['Price'].to_numpy()

multiplication_of_price_and_quantity = np.multiply(quantity_array, price_array)
print(f"multiplication_of_price_and_quantity: \n{multiplication_of_price_and_quantity}")

Month = pd.to_datetime(sales_data['Date']).dt.strftime('%m')

sales_data['Month'] = Month
print(sales_data.head())

unique_month = sales_data['Month'].unique()
print(f"Unique values in the 'Month' Column is: {unique_month}")

txt_df = sales_data[:5]
with open("sales_snapshot.txt", "w") as file:
    file.write(str(txt_df))
