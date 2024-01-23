import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as ptl
from sklearn.linear_model import LinearRegression
from scipy.stats import linregress
import statistics


# Question 1
def question_1():
    numbers_list = []
    result_numbers_list = []
    print("Enter the numbers and if you want to stop entering enter :q")
    while True:
        inputed_number = input("Enter Number: ")
        if inputed_number == ":q":
            break
        numbers_list.append(int(inputed_number))

    for _ in numbers_list:
        if _ % 2 == 0:
            result_numbers_list.append(_)

    return numbers_list


# print(question_1())

# Question 2
def question_2():
    with open("grades.txt", "r") as file:
        for line in file:
            split_line = line.strip().split(',')
            if int(split_line[1].strip()) >= 90:
                print(line.strip())


# question_2()


# Question 3

def question_3():
    df = pd.DataFrame({
        "Subject": ["Math", "Chemistry", "Biology"],
        "Score": [15, 10, 25]
    })

    average_scores = df.groupby('Subject')['Score'].mean()

    return average_scores


# print(question_3())


# Question 4

def question_4():
    students = ['John', 'Alice', 'Bob', 'Eva']
    scores = np.array([85, 92, 78, 89])

    filtered_students = np.array(students)[scores > 80]
    filtered_scores = scores[scores > 80]

    plt.plot(filtered_students, filtered_scores, marker="o", linestyle="-")

    plt.xlabel("students-axis")
    plt.ylabel("scores-axis")
    plt.title("Students&Scores")

    plt.show()


# question_4()

# Question 5

arr_positive = np.array([10, 25, 8, 42, 15, 7])
arr_mixed = np.array([-5, 20, -8, 15, -3, 10])
arr_float = np.array([3.5, 1.2, 7.8, 4.6, 2.1, 9.0])
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])


def question_5(array):
    maximum = np.max(array)
    minimum = np.min(array)

    return maximum, minimum


# question_5(arr_2d)


# Question 6

def question_6():
    x = np.array([[1, 6], [2, 7], [3, 8], [4, 9], [5, 10], [6, 11], [7, 12], [8, 13], [9, 14], [10, 15]])
    y = np.array([2, 4, 5, 4, 5, 6, 7, 8, 9, 10])

    model = LinearRegression()
    model.fit(x, y)
    y_pred = model.predict(x)

    print("Slope (Coefficient):", model.coef_)
    print("Intercept:", model.intercept_)

    plt.scatter(x[:, 0], y, color='blue', label='Actual Data')
    plt.plot(x[:, 0], y_pred, color='red', linewidth=2, label='Linear Regression Line')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Generated Data for Linear Regression')
    plt.show()


# question_6()

# Question 7

def question_7():
    data = {'X1': [1, 2, 3, 4, 5],
            'X2': [2, 3, 4, 5, 6],
            'Y': [5, 7, 9, 11, 13]}

    df = pd.DataFrame(data)
    result = linregress(x=df['X1', 'X2'], y=df['Y'])
    slope_x1, slope_x2 = result.slope
    intercept = result.intercept
    print(f"Intercept: {intercept}")
    print(f"Coefficients: X1={slope_x1}, X2={slope_x2}")
    new_data = {'X1': np.array([6, 7, 8]),
                'X2': np.array([7, 8, 9])}

    predicted_y = intercept + slope_x1 * new_data['X1'] + slope_x2 * new_data['X2']
    print(f"Predicted Y values for new data: {predicted_y}")


# question_7()

# Question 8

def question_8(numbers):
    mean = statistics.mean(numbers)
    variance = statistics.variance(numbers)
    std_dev = statistics.stdev(numbers)

    return mean, variance, std_dev


# mean, variance, std_dev = question_8([1, 2, 3, 4, 5])
# print(f"Mean: {mean}, Variance: {variance}, std_dev: {std_dev}")


# Question 9

def question_9():
    input_text = input("Enter a text: ")

    count_of_a = input_text.count('a')
    count_of_e = input_text.count('e')
    count_of_i = input_text.count('i')
    count_of_o = input_text.count('o')
    count_of_u = input_text.count('u')

    return count_of_a, count_of_e, count_of_i, count_of_o, count_of_u


# print(question_9())


# Question 10
def question_10():
    inventory = {
        'item1': {'quantity': 10, 'price': 19.99, 'category': 'electronics'},
        'item2': {'quantity': 5, 'price': 29.99, 'category': 'clothing'},
        'item3': {'quantity': 20, 'price': 4.99, 'category': 'groceries'},
        'item4': {'quantity': 15, 'price': 9.99, 'category': 'books'},
        'item5': {'quantity': 8, 'price': 49.99, 'category': 'electronics'},
        'item6': {'quantity': 30, 'price': 14.99, 'category': 'groceries'},
    }

    laptop_present = any(item_name.lower() == 'laptop' for item_name in inventory.keys())

    return laptop_present

# print(question_10())
