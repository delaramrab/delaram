def merge_matrix(c11, c12, c21, c22):
    number_of_size = len(c11)
    size = 2 * number_of_size

    total_matrix = [[0 for column in range(size)] for row in range(size)]

    for i in range(0, size):
        for j in range(0, size):
            if i <= (number_of_size - 1) and j <= (number_of_size - 1):
                total_matrix[i][j] = c11[i][j]
            elif i <= (number_of_size - 1) and j > (number_of_size - 1):
                total_matrix[i][j] = c12[i][j - number_of_size]
            elif i > (number_of_size - 1) and j <= (number_of_size - 1):
                total_matrix[i][j] = c21[i - number_of_size][j]
            else:
                total_matrix[i][j] = c22[i - number_of_size][j - number_of_size]

    return total_matrix


def multiply_matrix(matrix_1, matrix_2, n):
    result_matrix = [[0 for j in range(len(matrix_1[0]))] for i in range(len(matrix_2))]

    if n <= 2:

        p1 = (matrix_1[0][0] + matrix_1[1][1]) * (matrix_2[0][0] + matrix_2[1][1])
        p2 = (matrix_1[1][0] + matrix_1[1][1]) * matrix_2[0][0]
        p3 = matrix_1[0][0] * (matrix_2[0][1] - matrix_2[1][1])
        p4 = matrix_1[1][1] * (matrix_2[1][0] - matrix_2[0][0])
        p5 = (matrix_1[0][0] + matrix_1[0][1]) * matrix_2[1][1]
        p6 = (matrix_1[1][0] - matrix_1[0][0]) * (matrix_2[0][0] + matrix_2[0][1])
        p7 = (matrix_1[0][1] - matrix_1[1][1]) * (matrix_2[1][0] + matrix_2[1][1])

        result_matrix[0][0] = p1 + p4 - p5 + p7
        result_matrix[0][1] = p3 + p5
        result_matrix[1][0] = p2 + p4
        result_matrix[1][1] = p1 + p3 - p2 + p6

    else:
        (matrix_a11, matrix_a12, matrix_a21, matrix_a22) = partition_matrix(matrix_1)
        (matrix_b11, matrix_b12, matrix_b21, matrix_b22) = partition_matrix(matrix_2)
        (matrix_c11, matrix_c12, matrix_c21, matrix_c22) = partition_matrix(result_matrix)

        matrix_c11 = add(multiply_matrix(matrix_a11, matrix_b11, n // 2),
                         multiply_matrix(matrix_a12, matrix_b21, n // 2))
        matrix_c12 = add(multiply_matrix(matrix_a11, matrix_b12, n // 2),
                         multiply_matrix(matrix_a12, matrix_b22, n // 2))
        matrix_c21 = add(multiply_matrix(matrix_a21, matrix_b11, n // 2),
                         multiply_matrix(matrix_a22, matrix_b21, n // 2))
        matrix_c22 = add(multiply_matrix(matrix_a21, matrix_b12, n // 2),
                         multiply_matrix(matrix_a22, matrix_b22, n // 2))

        result_matrix = merge_matrix(matrix_c11, matrix_c12, matrix_c21, matrix_c22)

    return result_matrix


def partition_matrix(matrix):
    size_of_matrix = len(matrix)
    size_for_divide_matrix = size_of_matrix // 2

    matrix_a11 = [[0 for col in range(size_for_divide_matrix)] for row in range(size_for_divide_matrix)]
    matrix_a12 = [[0 for col in range(size_for_divide_matrix)] for row in range(size_for_divide_matrix)]
    matrix_a21 = [[0 for col in range(size_for_divide_matrix)] for row in range(size_for_divide_matrix)]
    matrix_a22 = [[0 for col in range(size_for_divide_matrix)] for row in range(size_for_divide_matrix)]

    for i in range(0, size_for_divide_matrix):
        for j in range(0, size_for_divide_matrix):
            matrix_a11[i][j] = matrix[i][j]
            matrix_a12[i][j] = matrix[i][j + size_for_divide_matrix]
            matrix_a21[i][j] = matrix[i + size_for_divide_matrix][j]
            matrix_a22[i][j] = matrix[i + size_for_divide_matrix][j + size_for_divide_matrix]

    return matrix_a11, matrix_a12, matrix_a21, matrix_a22


def add(matrix_a, matrix_b):
    size_of_matrix = len(matrix_a)
    result_matrix_c = [[0 for col in range(size_of_matrix)] for row in range(size_of_matrix)]

    for i in range(0, size_of_matrix):
        for j in range(0, size_of_matrix):
            result_matrix_c[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result_matrix_c


row_matrix_1 = int(input("Please insert the number of rows in matrix one: "))
column_matrix_1 = int(input("Please insert the number of column in matrix one: "))

row_matrix_2 = int(input("please insert the number of rows in matrix two: "))
column_matrix_2 = int(input("please insert the number of column in matrix two: "))

matrix1 = []
matrix2 = []

print("\nPlease insert the value in the matrix 1: ")

for row in range(row_matrix_1):
    temp = []
    for column in range(column_matrix_1):
        temp.append(int(input()))
    matrix1.append(temp)

for row in range(row_matrix_1):
    for column in range(column_matrix_1):
        print(f"{matrix1[row][column]: .1f}", end=" ")
    print()

print("\nPlease insert the value in the matrix 2: ")

for row in range(row_matrix_2):
    temp = []
    for column in range(column_matrix_2):
        temp.append(int(input()))
    matrix2.append(temp)

for row in range(row_matrix_2):
    for column in range(column_matrix_2):
        print(f"{matrix2[row][column]: .1f}", end=" ")
    print()

if column_matrix_1 == row_matrix_2:
    print(f"\n{multiply_matrix(matrix1, matrix2, row_matrix_1)}")
else:
    print("multiplication in not possible, row_matrix_2 must be equal with column_matrix_1")
