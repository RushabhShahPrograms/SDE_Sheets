'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
'''

def setZeroes(matrix):
    f1,f2 = False,False
    n,m = len(matrix),len(matrix[0])

    for i in range(n):
        if matrix[i][0] == 0:
            f1 = True
    
    for j in range(m):
        if matrix[0][j] == 0:
            f2 = True
    
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    if f1:
        for i in range(n):
            matrix[i][0] = 0
    if f2:
        for j in range(m):
            matrix[0][j] = 0

matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix1)
print(matrix1)

matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix2)
print(matrix2)