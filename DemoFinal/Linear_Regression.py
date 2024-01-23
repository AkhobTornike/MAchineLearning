import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LinearRegression

iris = sns.load_dataset("iris")

iris = iris[['petal_length', 'petal_width']]

X = iris['petal_length']
y = iris['petal_width']

# plt.scatter(X, y)
# plt.xlabel("Petal Length")
# plt.ylabel("Petal Width")
# plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=23)

# print(X_train)
X_train = np.array(X_train).reshape(-1, 1)
# print(X_train)

# print(X_test)
X_test = np.array(X_test).reshape(-1, 1)
# print(X_test)

lr = LinearRegression()
lr.fit(X_train, y_train)

c = lr.intercept_
m = lr.coef_


y_pred_train = lr.predict(X_train)

plt.scatter(X_train, y_train)
plt.plot(X_train, y_pred_train, color='red')
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Train")
plt.show()

# y_pred_test = lr.predict(X_test)
#
# plt.scatter(X_test, y_test)
# plt.plot(X_test, y_pred_test, color='red')
# plt.xlabel("Petal Length")
# plt.ylabel("Petal Width")
# plt.title("Test")
# plt.show()

