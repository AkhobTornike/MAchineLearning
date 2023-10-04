import os
import math


# work 1
def work_one():
    f = open("data.txt", "a")
    f.write("24\t")
    f.write("39\t")
    f.write("90\t\n")
    f.close()


# work 2
def work_two():
    folder_name = "myFiles"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    file_path = os.path.join(folder_name, "data1.txt")
    with open(file_path, "a") as file:
        for i in range(100):
            if i % 10 == 0:
                file.write(f"{i}\n")
            else:
                file.write(f"{i}\t")
    print(f"File 'data1.txt' has been created in the '{folder_name}' folder.")


# work 3
def work_three():
    folder_name = "myFiles1"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    for i in range(30):
        file_path = os.path.join(folder_name, f"data{i}.txt")
        with open(file_path, "a") as file:
            file.write("Programmer")
        print(f"File 'data{i}.txt' has been created in the '{folder_name}' folder.")


# work 4
def work_four():
    folder_name = "myFiles2"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    for i in range(30):
        file_path = os.path.join(folder_name, f"data{i}.txt")
        with open(file_path, "a") as file:
            for j in range(30):
                file.write(f"Programmer{j}")
        print(f"File 'data{i}.txt' has been created in the '{folder_name}' folder.")


# work 7
def work_seven():
    folder_name = "myFiles"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    file_path = os.path.join(folder_name, "function.txt")

    with open(file_path, "w") as file:
        for x in range(0, 201):
            x_value = x / 100.0
            result = (math.sin(x_value) + math.cos(x_value))
            file.write(f"{x_value:.2f}: {result:.4f}\n")


# work 9
def work_nine():
    folder_name = "myFiles"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    for i in range(10000):
        file_path = os.path.join(folder_name, f"{i}.txt")
        with open(file_path, "w") as file:
            file.write(f"{i}")
        print(f"File '{i}.txt' has been created in the '{folder_name}' folder.")


# work 10
def work_ten():
    dictionary = {
        1: 10,
        2: 20,
    }
    print(f"Before update {dictionary}")
    dictionary.update({
        3: 30,
        4: 40
                       })
    print(f"After First update {dictionary}")
    dictionary.pop(1)
    print(f"After Second update {dictionary}")


# work 11
def work_eleven():
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}

    combined_dict = {}
    combined_dict.update(dic1)
    combined_dict.update(dic2)
    combined_dict.update(dic3)
    print(combined_dict)


# work 12
def work_twelve():
    d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

    if 3 in d:
        print(d[3])


# work 13
def work_thirteen():
    d = {'x': 10, 'y': 20, 'z': 30}

    for key, value in d.items():
        print(f"{key} -> {value}")


# work 14
def work_fourteen():
    d = {}
    for i in range(1, 11):
        d.update({i: pow(i, 2)})
    print(d)


# work 18
def work_eighteen():
    t = {}

    for i in range(1, 100):
        x = list(t)
        if i % 5 == 0:
            x.append(i)
        t = tuple(x)

    print(t)
    print(len(t))


# work_one()
# work_two()
# work_three()
# work_four()
# work_seven()
# work_nine()
# work_ten()
# work_eleven()
# work_twelve()
# work_thirteen()
# work_fourteen()
# work_eighteen()
