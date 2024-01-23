import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from scipy.stats import linregress
# Question 1

def question_1():
    words_dictionary = {}
    print("Enter the numbers and if you want to stop entering enter : q")
    while True:
        word = input("Enter Any Word: ")
        if word == 'q':
            break
        words_dictionary[word] = len(word)

    return words_dictionary

# print(question_1())

# Question 2

def question_2():
    with open('temperatures.txt', 'r') as File:
        temperatures = []
        for line in File:
            temperature = line.strip().split(',')
            temperatures.append(int(temperature[1]))

    mean_of_temperatures = np.mean(temperatures)

    return mean_of_temperatures

# print(question_2())


# Question 3

def question_3():
    sales_data = pd.DataFrame({'Product': ['A', 'B', 'C'],
                               'Revenue': [1200, 800, 1500]})

    filter_data = sales_data[sales_data['Revenue'] > 1000]

    return filter_data


# print(question_3())


# Question 4

def question_4():
    x = [1, 2, 3, 4, 5]
    y = [10, 12, 8, 15, 14]

    plt.scatter(x, y, marker='o', color='red', linestyle='-')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Sales')

    plt.show()


# question_4()

# Question 5

def question_5():
    arr = np.array([2, 4, 6, 8, 10])

    mean = np.mean(arr)
    median = np.median(arr)

    return mean, median

# print(question_5())

# Question 6

def question_6():
    np.random.seed(42)
    x = 2 * np.random.rand(100, 1)
    y = 4 + 3 * x + np.random.randn(100, 1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print('MSE: ', mse)
    print(f"R2: {r2}")

    plt.scatter(x_test, y_test, marker='o', color='black', label='Actual Data')
    plt.plot(x_test, y_pred, color='red', linestyle='-', label='Predicted Data')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Sales')
    plt.legend()

    plt.show()


# question_6()

# Question 7

def question_7():
    data = {'X1': [1, 2, 3, 4, 5],
            'X2': [2, 3, 4, 5, 6],
            'Y': [5, 7, 9, 11, 13]}

    df = pd.DataFrame(data)

    result = linregress(x=df['X1', 'X2'], y=df['Y'])
    slope_1, slope_2 = result.slope
    intercept = result.intercept

    
