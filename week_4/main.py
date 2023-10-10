import numpy as np
import math


# work 1
def work_one():
    string_input = input("Enter eny text: ")

    symbol_count = len([char for char in string_input if char != ' '])

    print(symbol_count)


# work 2
def work_two():
    string_input_1 = input("Enter eny text: ")
    string_input_2 = input("Enter eny text: ")

    final_string = string_input_1 + ' ' + string_input_2

    print(final_string)


# work 3
def work_three():
    string_input = input("Enter eny text: ")

    special_symbol_count = len([char for char in string_input if char == 'a'])

    print(f"In your entered text is {special_symbol_count} amount of 'a'")


# work 4
def work_four():
    fruits = ['Banana', 'Watermelon', 'Apple']

    [print(fruit) for fruit in sorted(fruits)]


# work 5
def work_five():
    text = 'სწავლის ძირი მწარე არის, კენწეროში გატკბილდების'

    special_symbol_count = len([char for char in text[:20] if char == 'ს'])

    print(f"In first 20 symbol from '{text}' is {special_symbol_count} amount of 'ს'")


# work 9
def work_nine():
    text = 'Hello, this is example of string. Please, write this text and do some exercises.'

    changed_text = text.replace(' is ', ' were ')

    print(changed_text)


# work 10
def work_ten():
    text = 'Hello, this is example of string. Please, write this text and do some exercises.'

    print(len(text.split()))


# work 11
def work_twelve():
    text = 'Have a nice day'

    characters = [char for char in text if char != ' ']
    characters.reverse()

    [print(char) for char in characters]


# work 12
def work_eleven():
    text = "tornike.akhobadze@gmail.com"

    print(text.index('@'))


# work 13
def work_thirteen():
    name = str(input("Enter your name: "))
    l_name = str(input("Enter your family name: "))

    if name and l_name:
        email = name + '.' + l_name + '@edu.ge'
        return f'Your email is {email}'
    else:
        print("Both name and family name are required. Please try again.")
        return work_thirteen()


# work 14
def work_fourteen():
    string = str(input("Enter something: "))

    char_array = [char for char in string if char != ' ']
    array_size = len(char_array)

    # configure if task is possible
    t1 = math.sqrt(array_size)
    t2 = int(t1)

    if t1 == t2:
        matrix = [char_array[i:i + t2] for i in range(0, array_size, t2)]
        return matrix
    else:
        return "Error - The length of the character array is not a multiple of 3."


# work 15
def work_fifteen():
    random_vector_1 = np.random.rand(3)
    random_vector_2 = np.random.rand(3)

    sum_vector = random_vector_1 + random_vector_2
    print(f"sum of vectors {sum_vector}")


# work 16
def work_sixteen():
    matrix_1 = np.array([[1, 2, 3],
                         [4, 5, 6]])

    matrix_2 = np.array([[7, 8],
                         [9, 10],
                         [11, 12]])

    sum_matrix = matrix_1 + matrix_2
    return sum_matrix


# work 17
def work_seventeen():
    random_vector_1 = np.random.rand(3)
    random_vector_2 = np.random.rand(3)

    multiple_vector = np.dot(random_vector_1, random_vector_2)
    return multiple_vector


# work 18
def work_eighteen():
    matrix_1 = np.array([[1, 2, 3],
                         [4, 5, 6]])

    matrix_2 = np.array([[7, 8],
                         [9, 10],
                         [11, 12]])

    multiple_matrix = np.dot(matrix_1, matrix_2)
    return multiple_matrix


# work 19
def work_nineteen():
    matrix = np.random.randint(0, 10, size=(3, 3))

    return matrix


# work 20
def work_twenty():
    matrix = np.random.randint(0, 10, size=(10, 10))

    print(matrix)

    element_to_delete = int(input("Enter any number from matrix: "))
    print(f"\n{element_to_delete}")

    mask = matrix != element_to_delete

    new_matrix = matrix[mask]

    return new_matrix


# work 21
def work_twenty_one():
    matrix = np.random.randint(0, 10, size=(10, 10))
    for index, row in enumerate(matrix):
        print(f"Row {index}: {row}")

    row_to_delete = int(input("Enter index of row which one i want to delete: "))
    final_matrix = np.delete(matrix, row_to_delete, axis=0)

    return final_matrix


# work 22
def work_twenty_two():
    matrix = np.random.randint(0, 10, size=(10, 10))
    print(f"Before changes {matrix}")

    matrix[matrix == 0] = 1
    return f"After changes {matrix}"


# work 23
def work_twenty_three():
    chess_board = np.zeros((8, 8), dtype=int)
    chess_board[::2, ::2] = 1
    chess_board[1::2, 1::2] = 1

    chess_board = chess_board.astype('U1')
    chess_board[1] = 'P'
    chess_board[6] = 'P'
    chess_board[::7, ::7] = 'R'
    chess_board[::7, 1::5] = 'B'
    chess_board[::7, 2::3] = 'N'
    chess_board[::7, 3] = 'Q'
    chess_board[::7, 4] = 'K'

    return chess_board


# work 24
def work_twenty_four():
    matrix_1 = np.random.randint(0, 10, size=(10, 10))
    matrix_2 = np.random.randint(0, 10, size=(10, 10))

    final_matrix = np.concatenate((matrix_1, matrix_2), axis=0)
    final_vector = final_matrix.reshape(-1)

    return final_vector


print(work_twenty_four())
# print(work_twenty_three())
# print(work_twenty_two())
# print(work_twenty_one())
# print(work_twenty())
# print(work_nineteen())
# print(work_eighteen())
# print(work_seventeen())
# print(work_sixteen())
# print(work_fifteen())
# print(work_fourteen())
# print(work_thirteen())
# work_eleven()
# work_twelve()
# work_ten()
# work_nine()
# work_five()
# work_four()
# work_three()
# work_two()
# work_one()
