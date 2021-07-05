from typing import List


def matrix(matrix1: List[List[float]], matrix2: List[List[float]]) -> List[list]:

    matrix1_row = len(matrix1)
    matrix1_column = len(matrix1[0])
    matrix2_row = len(matrix2)
    matrix2_column = len(matrix2[0])

    if matrix1_column != matrix2_row:
        raise Exception("number of the column in first matrix must be equal to number of the rows in the second number")

    result_matrix = []

    for row in range(matrix1_row):
        row_result = []
        for column in range(matrix2_column):
            temp = 0
            for k in range(matrix2_row):

                temp += matrix1[row][k] * matrix2[k][column]

            row_result.append(temp)

        result_matrix.append(row_result)

    return result_matrix


matrix_a = [[2, 3, 6],
            [5, -1, 12]]

matrix_b = [[1, 0, 4, 7],
            [2, -3, 6, 2],
            [5, 8, 9, 6]]

print(matrix(matrix_a, matrix_b))
