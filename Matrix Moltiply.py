from typing import List


def multiply_matrix(matrix_a, matrix_b) -> List[List[float]]:

    result = [[0 for j in range(len(matrix_b[0]))] for i in range(len(matrix_a))]

    for row in range(len(matrix_a)):
        for column in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result[row][column] += matrix_a[row][k] * matrix_b[k][column]

    return result


row_matrix_1 = int(input("Please insert the number of rows in matrix one: "))
column_matrix_1 = int(input("Please insert the number of column in matrix one: "))

row_matrix_2 = int(input("please insert the number of rows in matrix two"))
column_matrix_2 = int(input("please insert the number of column in matrix two"))

matrix_1 = []
matrix_2 = []

print("\nPlease insert the value in the matrix 1: ")

for row in range(row_matrix_1):
    temp = []
    for column in range(column_matrix_1):
        temp.append(int(input()))
    matrix_1.append(temp)

for row in range(row_matrix_1):
    for column in range(column_matrix_1):
        print(matrix_1[row][column], end=" ")
    print()



print("\nPlease insert the value in the matrix 2: ")

for row in range(row_matrix_2):
    temp = []
    for column in range(column_matrix_2):
        temp.append(int(input()))
    matrix_2.append(temp)


for row in range(row_matrix_2):
    for column in range(column_matrix_2):
        print(matrix_1[row][column], end=" ")
    print()


if column_matrix_1 == row_matrix_2:
    print(f"\nmultiply_matrix(matrix_1, matrix_2)")
else:
    print("multiplication in not possible, row_matrix_2 must be equal with column_matrix_1")



