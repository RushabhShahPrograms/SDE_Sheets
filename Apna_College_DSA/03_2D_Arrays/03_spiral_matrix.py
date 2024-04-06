'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''

def spiralOrder(matrix):
    res = []
    m,n = len(matrix),len(matrix[0])
    rowstart,rowend,colstart,colend = 0,m,0,n

    while rowstart < rowend and colstart < colend:
        for k in range(colstart,colend):
            res.append(matrix[rowstart][k])
        rowstart += 1

        for k in range(rowstart,rowend):
            res.append(matrix[k][colend - 1])
        colend -= 1

        if rowstart < rowend:
            for k in range(colend - 1,colstart - 1,-1):
                res.append(matrix[rowend - 1][k])
            rowend -= 1
        
        if colstart < colend:
            for k in range(rowend - 1,rowstart-1,-1):
                res.append(matrix[k][colstart])
            colstart += 1
    return res

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix1))

matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix2))