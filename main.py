
# Задание 1
print("Задание 1\n")
for i in range(1, 101):
    if i % 7 == 0:
        print(i)
print()

# Задание 2
print("Задание 2\n")
num = int(input("Введите число: "))
i = num - 1
while i >= 1:
    num = num * i
    if i > 1:
        i -= 1
        continue
    if i == 1:
        print(num)
        break
print()

# Задание 3
print("Задание 3\n")
for i in range(1, 11):
    print("2 x", i, " = ", 2 * i, "\t3 x", i, " = ", 3 * i, "\t4 x", i, " = ", 4 * i, "\t5 x", i, " = ", 5 * i)
print()

# Задание 4
print("Задание 4\n")
width = int(input("Введите ширину: "))
height = int(input("Введите высоту: "))
z = '*'
for i in range(width):
    print(z, end=" ")
print()
for j in range(height):
    print(z)

for i in range(width):
    print(z, end=" ")
print()

# Задание 5
print("\nЗадание 5\n")
list_1 = [0, 5, 2, 4, 7, 1, 3, 19]
for i in list(list_1):
    if i % 2 != 0:
        print(i)
print()

# Задание 6
from random import randint
print("Задание 6\n")
list_ran_nums_1 = []
list_ran_nums_2 = []
for i in range(4):
    num = randint(1, 101)
    list_ran_nums_1.append(num)
    doubled_num = num * 2
    list_ran_nums_2.append(doubled_num)
print(list_ran_nums_1)
print(list_ran_nums_1 + list_ran_nums_2)
print()

# Задание 7
print("Задание 7\n")
list_of_salaries = []
for i in range(12):
    num_of_salaries = randint(7500, 15001)
    list_of_salaries.append(num_of_salaries)
print(list_of_salaries)
summ_of_salaries = sum(list_of_salaries)
print("Сумма: ", summ_of_salaries)
print("Средняя зарплата: ", summ_of_salaries // 12)
print()

# Задание 8
print("Задание 8\n")
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
print(matrix)
first_row = matrix[0]
second_row = matrix[1]
third_row = matrix[2]
fourth_row = matrix[3]
sumOfFirst_row = first_row[0] + first_row[1] + first_row[2] + first_row[3]
sumOfSecond_row = second_row[0] + second_row[1] + second_row[2] + second_row[3]
sumOfThird_row = third_row[0] + third_row[1] + third_row[2] + third_row[3]
sumOfFourth_row = fourth_row[0] + fourth_row[1] + fourth_row[2] + fourth_row[3]
SumOfMatrix = sumOfFirst_row + sumOfSecond_row + sumOfThird_row + sumOfFourth_row
print("Сумма элементов матрицы: ", SumOfMatrix)
print()

# Дополнительное задание 3
print("Дополнительное задание 3\n")
size_of_list = int(input("Введите размер списка: "))
my_list = []
for i in range(size_of_list):
    listNum = randint(1, 1001)
    my_list.append(listNum)
print(my_list)
my_list.reverse()
print("Перевернутый список: ", my_list)