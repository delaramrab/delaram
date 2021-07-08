from typing import List


def multiply_matrix(matrix_a, matrix_b) -> List[List[float]]:

    result = [[0 for j in range(len(matrix_b[0]))] for i in range(len(matrix_a))]

    for row in range(len(matrix_a)):
        for column in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result[row][column] += matrix_a[row][k] * matrix_b[k][column]

    return result


matrix_1 = [[2, 3, 6],
            [5, -1, 12]]

matrix_2 = [[1, 0, 4, 7],
            [2, -3, 6, 2],
            [5, 8, 9, 6]]

print(multiply_matrix(matrix_1, matrix_2))
