import random
from collections import Counter

# work 1!
def work_one():
    list = []
    for i in range(0, 3, 1):
        list.append(int(input("Enter a number: ")))

    return max(list)


# work 2!
def work_two():
    for i in range(10):
        print(random.randint(1, 10))


# work 3!
work_three = lambda num1, num2: print((num1 + num2) / 2)


# work 4!
def work_four(number):
    if number % 2 == 0:
        return False
    else:
        return True


# work 5!
def work_six():
    numbs = [1, 2, 3, 4, 5]

    total_sum = sum(numbs)
    print(f'sum of elements is {total_sum}')

    print(f'maximum from the list is {max(numbs)}')

    print(f'minimum from the list is {min(numbs)}')

    print(f'Arithmetic average is {sum(numbs) / len(numbs)} ')

    numbs.append(102)
    print(numbs)

    numbs[2] = 205
    print(numbs)

    del numbs[4]
    print(numbs)

    print(sorted(numbs))


# work 7!
def work_seven():
    numbs = [1, 4, 52, 6, 76, 12, 35]
    for i in range(len(numbs) - 1):
        if numbs[i] % 2 == 1:
            numbs.pop(i)
        else:
            pass
    print(numbs)


# work 8!
def work_eight():
    numbs = []
    for i in range(10):
        numbs.append(random.randint(25, 110))

    print(f'From list {numbs} minimum is {min(numbs)}')


# work 9!
def work_nine():
    numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbs)
    print(numbs)


# work 10!
def work_ten():
    numbs = [1, 5, 23, 5, 12, 2, 5, 1, 18, 5]
    count_dict = Counter(numbs)

    most_common_element, count = count_dict.most_common(1)[0]

    print(f'The most common number is {most_common_element}, which appears {count} times.')


# work 11!
def work_eleven():
    input_string = 'python php pascal javascript java c++'
    word_list = input_string.split()

    longest_word = ""
    max_length = 0

    for word in word_list:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    print("The longest word is:", longest_word)


# work 12!
def work_twelve():
    numbs = []
    for i in range(11):
        numbs.append(random.randint(25, 110))

    sorted(numbs)

    print(numbs)

    average = sum(numbs) / len(numbs)

    if len(numbs) % 2 == 0:
        mediana = (numbs[len(numbs) // 2] + numbs[(len(numbs) // 2) - 1]) / 2
        print(numbs[len(numbs) // 2])
        print(numbs[(len(numbs) // 2) - 1])
    elif len(numbs) % 2 == 1:
        mediana = numbs[int(len(numbs) / 2)]

    count_dict = Counter(numbs)
    most_common_elements = count_dict.most_common()

    if most_common_elements[0][1] == len(numbs):
        moda = "There is no any"
    else:
        moda = most_common_elements[0][0]

    print("The most common element is:", moda)
    print(f'mediana is {mediana}')

# work_twelve()
# print(work_eleven())
# print(work_ten())
# print(work_nine())
# print(work_eight())
# print(work_seven())
# print(work_six())
# print(work_four(12))
# work_three(3, 7)
# work_three(15, 12)
# work_three(1, 9)
# print(work_two())
# print(f'maximum is ', work_one())
