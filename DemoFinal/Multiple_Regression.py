# Pandas
# import pandas as pd
# from pprint import pprint
# data = pd.read_excel('data.xlsx')
#
# pprint(data)
#
# Names = data['Name'].tolist()
# Ages = data['Age'].tolist()
# Scores = data['Score'].tolist()
# print(f"Names: {Names}")
# print(f"Ages: {Ages}")
# print(f"Score: {Scores}")
#
# Alice = data.iloc[0]
# Bob = data.iloc[1]
# Charlie = data.iloc[2]
# print(f"Alice: {Alice}")
# print(f"Bob: {Bob}")
# print(f"Charlie: {Charlie}")
#
# condition = data['Age'] >= 25
#
# new_data = data[condition]
# pprint(new_data)
#
# working_data = data
# working_data['Grades'] = pd.cut(working_data['Score'], bins=[0, 70, 80, float('inf')], labels=['C', 'B', 'A'])
#
# pprint(working_data)
#
# working_data.to_excel('modified_data.xlsx', sheet_name='ModifiedSheet', index=False)
#
# mean_score = np.mean(Scores)
# print(f"Mean Score: {mean_score}")
#mathplotlib
# from matplotlib import pyplot as plt
#
# x = np.arange(0, 10, 0.1)
# y = np.sin(x)
#
# plt.plot(x, y)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()
#
#
# x = [1, 2, 3, 4, 5]
# y = [10, 12, 5, 8, 7]
#
# plt.scatter(y, x, color='red')
# plt.xlabel("Y-axis")
# plt.ylabel("X-axis")
# plt.show()
#
#
# categories = ['Category A', 'Category B', 'Category C']
# values = [15, 25, 10]
#
# plt.bar(categories, values)
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.legend(categories)
# plt.title("Sales by Category")
# plt.savefig('chart.png')
# plt.show()
# Numpy
# import numpy as np
#
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([0, 1, 0, 1, 0])
#
# print(f"arr1: {arr1}; \narr2: {arr2}")
#
#
# result = np.array([arr1, arr2])
# print(f"result: {result}")
#
# arr3 = np.array([10, 20, 30, 40, 50])
#
# print(f"arr3: {arr3[2]}")
# split_arr3 = arr3[1:4]
# print(f"arr3 split: {split_arr3}")
#
# arr3 = np.append(arr3, [60, 70])
# print(arr3)
#
# arr4 = np.array([4, 8, 2, 5, 1, 6])
# arr4_mean = np.mean(arr4)
# arr4_std = np.std(arr4)
#
# print(f"Mean of arr4: {arr4_mean}")
# print(f"Standard deviation of arr4: {arr4_std}")
#
#
# matrix1 = np.array([[1, 2], [3, 4]])
# matrix2 = np.array([[5, 6], [7, 8]])
#
# result_matrix = np.dot(matrix1, matrix2)
# print(f"Matrix 1: {matrix1}; \nMatrix 2: {matrix2}; \nResult of Matrix Multiplication: {result_matrix}")
#
# scipy, sklearn
# from scipy.stats import linregress
# np.random.seed(42)
# X = 2 * np.random.rand(100, 1)
# y = 4 + 3 * X + np.random.randn(100, 1)
#
# slope, intercept, r_value, p_value, std_err = linregress(X.flatten(), y.flatten())
#
# print(f"SciPy Linear Regression Results:")
# print(f"Slope: {slope}")
# print(f"Intercept: {intercept}\n")
#
# from sklearn.linear_model import LinearRegression
#
# model = LinearRegression()
# model.fit(X, y)
#
# print(f"Coefficients: {model.coef_}")
# print(f"Intercept: {model.intercept_}\n")
#
# np.random.seed(42)
# X_multi = 2 * np.random.rand(100, 2)
# y_multi = 4 + 3 * X_multi[:, 0] + 5 * X_multi[:, 1] + np.random.randn(100)
#
# model = LinearRegression()
# model.fit(X_multi, y_multi)
#
# print(f"Coefficients: {model.coef_}")
# print(f"Intercept: {model.intercept_}\n")


import pandas as pd
from pprint import pprint
# from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
from scipy.stats import linregress
import numpy as np

np.random.seed(42)
data = np.random.randn(100)
np.random.seed(21)
data2 = np.random.randn(100)

Mean = np.mean(data)
Median = np.median(data)

print(f"Mean: {Mean}; \nMedian: {Median}")

Variance = np.var(data)
Standard_deviation = np.std(data)

print(f"Variance: {Variance}; \nStandard: {Standard_deviation}")

percentile_of_25 = np.percentile(data, 25)
percentile_of_75 = np.percentile(data, 75)

print(f"25% of Percentile: {percentile_of_25}; 75% of Percentile: {percentile_of_75}")

pprint(f"data: \n{data}")
pprint(f"data2: \n{data2}")

correlation_between_data_and_data1 = np.correlate(data, data2)

print(f"correlation_between_data_and_data1: {correlation_between_data_and_data1}")


