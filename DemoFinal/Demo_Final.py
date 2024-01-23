# Question 1
from matplotlib import pyplot as plt
from pyexpat import model


def question_1():
    amount_of_numbers = int(input("Enter how many numbers you want to sum: "))
    print(amount_of_numbers)

    numbers_list = []
    for _ in range(1, amount_of_numbers + 1):
        numbers_list.append(int(input(f"Enter the number{_}: ")))

    return sum(numbers_list)


# print(question_1())


# Question 2
def question_2():
    numbers_from_data = []
    with open("data.txt", "r") as file:
        for line in file:
            numbers_from_data.append(int(file.readline()))
            numbers_from_data.append(int(line.strip()))

    return sum(numbers_from_data)

# print(question_2())


# Question 3
import pandas as pd


def question_3():
    df = pd.DataFrame({
        "Name": ["John", "Smith", "Toko"],
        "Age": [25, 25, 25],
        "Score": [60, 115, 85]
    })

    filter_df = df[df["Score"] > 80]

    return filter_df


# print(question_3())

# Question 4
import  matplotlib.pyplot as plt


def question_4():
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 7, 25, 12]

    plt.plot(x, y, marker="o", linestyle="-")

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Line Plot of Data Points")

    plt.show()

# question_4()

# Question 5
import numpy as np


def question_5():
    arr = np.array([2, 4, 6, 8, 10])

    mean = np.mean(arr)
    standard_deviation = np.std(arr)
    median = np.median(arr)

    print(mean)
    print(standard_deviation)
    print(median)

# Question 6
from sklearn.linear_model import LinearRegression


def question_6():
    np.random.seed(42)
    X = 2 * np.random.rand(100, 1)
    Y = 4 + 3 * X + np.random.randn(100, 1)

    plt.scatter(X, Y, color='blue', label='Generated Data')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Generated Data for Linear Regression')
    plt.show()

    model = LinearRegression()
    model.fit(X, Y)

    print(f'Slope (Coefficient): {model.coef_[0][0]}')
    print(f'Intercept: {model.intercept_[0]}')

    X_new = np.array([[0], [2]])
    Y_pred = model.predict(X_new)

    plt.scatter(X, Y, color='blue', label='Generated Data')
    plt.plot(X_new, Y_pred, color='red', label='Linear Regression')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Linear Regression')
    plt.show()

# question_6()


# Question 7
from scipy.stats import linregress


def question_7():
    data = {'X1': [1, 2, 3, 4, 5],
            'X2': [2, 3, 4, 5, 6],
            'Y': [5, 7, 9, 11, 13]}

    # Creating a DataFrame
    df = pd.DataFrame(data)

    # Performing multiple regression
    result = linregress(x=df['X1'], y=df['Y'])
    slope_x1 = result.slope

    result = linregress(x=df['X2'], y=df['Y'])
    slope_x2 = result.slope

    intercept = result.intercept

    # Displaying the regression coefficients
    print(f"Intercept: {intercept}")
    print(f"Coefficients: X1={slope_x1}, X2={slope_x2}")

    # Predicting Y for new data
    new_data = {'X1': np.array([6, 7, 8]),
                'X2': np.array([7, 8, 9])}

    predicted_y = intercept + slope_x1 * new_data['X1'] + slope_x2 * new_data['X2']

    # Displaying the predicted Y values for new data
    print("Predicted Y values for new data:")
    print(predicted_y)

# question_7()

# Question 9

def question_9():
    inputed = input("Enter:")

    return inputed[::-1]

# question_9()


# Question 10
def question_10():
    students = pd.DataFrame({
        "Name": ["John", "Smith", "Toko"],
        "Age": [25, 25, 25],
        "Score": [60, 115, 85]
    })

    new_student = pd.Series({"Name": "Gio", "Age": 30, "Score": 145})

    students = students._append(new_student, ignore_index=True)

    return students

# print(question_10())
