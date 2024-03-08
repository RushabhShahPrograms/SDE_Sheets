'''
Write a program to print the shape of a matrix
'''

def print_shape(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0
    return  (num_rows, num_cols)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
shape = print_shape(matrix)
print("The shape of the matrix is: ",shape)