matrix_a = [[2, 3, 6],
            [5, -1, 12]]

matrix_b = [[1, 0, 4, 7],
            [2, -3, 6, 2],
            [5, 8, 9, 6]]

result = [[0, 0, 0, 0],
          [0, 0, 0, 0]]


for row in range(len(matrix_a)):
    for column in range(len(matrix_b[0])):
        for k in range(len(matrix_b)):
            result[row][column] += matrix_a[row][k] * matrix_b[k][column]


for member in result:
    print(member)
