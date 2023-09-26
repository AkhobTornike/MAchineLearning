def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# work 1
def work_one():
    return 4 - pow(2, 3) + 5 * 2 - 3 / 2


# work 2
def work_second(number):
    binary = bin(number)[2:]
    return binary


# work 3
def work_third():
    user_working_time = float(input("Please Enter Time you have been worked: "))
    user_salary_per_hour = float(input("Please Enter Your salary for one hour: "))
    print("hours: ", user_working_time)
    print("salary: ", user_salary_per_hour)

    return user_salary_per_hour * user_working_time


# work 4
def work_four():
    num1 = float(input("Please Enter First number: "))
    num2 = float(input("Please Enter Second number: "))
    num3 = float(input("Please Enter Third number: "))

    return (num1 + num2 + num3) / 3


# work 5
def work_fifth():
    user_age = int(input("Please Enter Your Age: "))

    return f'In {(100 - user_age)} Years later You will be 100 Years old'


# work 6
def work_six():
    number = float(input("Please Enter any number: "))
    if number > 0:
        return 'Number is Positive'
    else:
        pass


# work 7
def work_seven(number):
    if number % 10 == 0:
        return 'Number ends with 0'
    else:
        return 'Number does not ends with 0'


# work 8
def work_eight(num1, num2):
    if num1 > 10 and num2 > 10:
        return (num1 + num2) / 2
    else:
        return num1 * num2


# work 9
def work_nine(number):
    return f' Last digit is {number % 10}'


# work 10
def work_ten(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return f'{year} is not Nakiani'
        else:
            return f'{year} is Nakiani'


# work 11
def work_eleven():
    for i in range(20, 125, 5):
        print(i)


# work 12
def work_twelve():
    for i in range(200, 25, -8):
        print(i)


# work 13
def work_thirteen(num1, num2):
    list1 = []
    list2 = []

    for i in range(1, num1, 1):
        if num1 % i == 0:
            list1.append(i)

    for j in range(1, num2, 1):
        if num2 % j == 0:
            list2.append(j)

    return [element for element in list1 if element in list2]


# work 14
def work_fourteen():
    list = []
    number = 0
    for i in range(0, 10, 1):
        list.append(float(input("Please Enter Number: ")))

    for i in range(0, len(list), 1):
        number += list[i]

    return number / len(list)


# work 15
def work_fifteen():
    result = 0
    for i in range(1, 101, 1):
        if i % 2 == 0:
            result += i
    return result


# work 16
def work_sixteen():
    for i in range(1500, 2100, 1):
        if i % 7 == 0 and i % 5 == 0:
            print(i)
        else:
            pass

# work 17
def work_seventeen():
    numbers = 0
    for i in range(1500, 2100, 1):
        if i % 7 == 0 and i % 5 == 0:
            numbers += i
        else:
            pass
    return numbers


# work 18
def work_eighteen():
    result = 0
    while result <= 20000:
        for i in range(1500, 2100, 1):
            if i % 7 == 0 and i % 5 == 0:
                result += i
                print(i)
                if result + i > 20000:
                    break
        print('result is', result)
        if result + i >= 20000:
            break


# work 19
def work_nineteen():
    for i in range(1500, 2100, 5):
        print(i)


# work 20
def work_twenty():
    for num in range(15, 151, 5):
        if num in [50, 75, 80]:
            continue
        print(num)


# work 21
def work_twentyone(num1, num2):
    list1 = []
    list2 = []
    for i in range(1, num1, 1):
        if num1 % i == 0:
            list1.append(i)

    for i in range(1, num2, 1):
        if num2 % i == 0:
            list2.append(i)
    return max([element for element in list1 if element in list2])


# work 22
def work_twenty_two(num1, num2):
    if num1 > num2:
        for i in range(1, num2+1, 1):
            if (num1 * i) % num2 == 0:
                return (num1 * i)
    elif num2 > num1:
        for i in range(1, num1+1, 1):
            if (num2 * i) % num1 == 0:
                return (num2 * i)
    else:
        return num1 * 2


# work 23
def work_twenty_three():
    result = 0
    for i in range(0, 10, 1):
        number = int(input("Enter eny number: "))
        if number % 2 != 0:
            if number > result:
                result = number
    return result


# work 24
def work_twenty_four(number):
    list = []
    for i in range(number, 0, -1):
        if number % i == 0:
            list.append(i)
    list.reverse()
    return list


# work 25
def work_twenty_five(number):
    list = []
    for i in range(1, number+1, 1):
        if number % i == 0:
            list.append(i)
    if len(list) > 2:
        print('number is not easy')
        return False
    else:
        print('number is easy')
        return True


# work 26
def work_twenty_six():
    for i in range(2, 1000, 1):
        list = []
        for j in range(1, i+1, 1):
            if i % j == 0:
                list.append(j)
        if len(list) > 2:
            pass
        else:
            print(i)


# work 27
def work_twenty_seven():
    a, b = 0, 1
    while a <= 100:
        print(a, end=' ')
        a, b = b, a + b


# work 28
def work_twenty_eight():
    number = int(input("Enter a number: "))
    sum_of_digits = 0
    number_str = str(number)
    for digit in number_str:
        sum_of_digits += 1

    print("Sum of digits:", sum_of_digits)


# work 29
def work_twenty_nine():
    number = int(input("Enter a number: "))
    sum_of_digits = 0
    number_str = str(number)
    for digit in number_str:
        sum_of_digits += int(digit)

    print("Sum of digits:", sum_of_digits)


# work 30
def work_thirty():
    num = int(input("Enter a number: "))
    reversed_num = int(str(num)[::-1])
    print("Reversed number:", reversed_num)


# work 31
def work_thirty_one():
    num = int(input("Enter a number: "))
    reversed_num = int(str(num)[::-1])
    if num == reversed_num:
        print(f'number {num} is a palindrom')


# work 32
def work_thirty_two():
    num = int(input("Enter a number: "))
    factorial = 1
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    elif num == 0:
        print("Factorial of 0 is 1.")
    else:
        for i in range(1, num + 1):
            factorial *= i
        print("Factorial of", num, "is", factorial)


# work 33
def work_thirty_three(num):
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    elif num == 0:
        print("Factorial of 0 is 1.")
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i

        print("Factorial of", num, "is", factorial)

    num = int(input("Enter a number: "))


# print(work_thirty_three())
# print(work_thirty_two())
# print(work_thirty_one())
# print(work_thirty())
# print(work_twenty_nine())
# print(work_twenty_eight())
# print(work_twenty_seven())
# print(work_twenty_six())
# print(work_twenty_five(13))
# print(work_twenty_four(18))
# print(work_twenty_three())
# print(work_twenty_two(4, 9))
# print(work_twentyone(32, 123))
# print(work_twenty())
# print(work_nineteen())
# print(work_eighteen())
# print(work_seventeen())
# print(work_sixteen())
# print(work_fifteen())
# print(work_fourteen())
# print(work_thirteen(15, 18))
# print(work_twelve())
# print(work_eleven())
# print(work_ten(2100))
# print(work_nine(12453))
# print(work_eight(2, 15))
# print(work_seven(30))
# print(work_six())
# print(work_fifth())
# print(work_four())
# print(work_third())
# print(work_second(13))
# print(work_one())
