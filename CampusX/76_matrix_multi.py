'''
Write a program to perform matrix multiplication on 2 matrices
'''

def matrix_multiply(matrix1,matrix2):
    if len(matrix1[0]) != len(matrix2):
        return "Error: the number of columns in the first matrix must be equal to the number of rows in the second matrix"
    
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]

print(matrix_multiply(matrix1, matrix2))