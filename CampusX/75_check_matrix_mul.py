'''
Write a program that can check if you can perform matrix multiplication on 2 matrices
'''

def can_multiply(matrix1,matrix2):
    num_cols_matrix1 = len(matrix1[0]) if matrix1 else 0

    num_rows_matrix2 = len(matrix2)

    return num_cols_matrix1 == num_rows_matrix2

matrix1 = [[1,2,3],[4,5,6]]
matrix2 = [[1,2],[3,4],[5,6]]

can_multiply_result = can_multiply(matrix1,matrix2)
print("Can perform matrix multiplication: ",can_multiply_result)