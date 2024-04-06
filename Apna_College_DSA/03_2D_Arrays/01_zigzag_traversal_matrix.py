'''
Given a 2D matrix, print all elements of the given matrix in diagonal order. For example, consider the following 5 X 4 input matrix.  

Example:

1     2     3     4
5     6     7     8
9    10    11    12
13    14    15    16
17    18    19    20
Diagonal printing of the above matrix is

1
5 2
9 6 3
13 10 7 4
17 14 11 8
18 15 12
19 16
20

'''

ROW = 5
COL = 4

def diagonalOrder(matrix):
    for line in range(1,(ROW+COL)):
        start_col = max(0,line - ROW)
        count = min(line, (COL - start_col),ROW)
        for j in range(0,count):
            print(matrix[min(ROW,line)-j-1]
                  [start_col + j],end="\t")
        print()

def printMatrix(matrix):
    for i in range(0,ROW):
        for j in range(0,COL):
            print(matrix[i][j],end="\t")
        print()

M = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16],
     [17,18,19,20]]
print("Given matrix is")
printMatrix(M)

print("\nDiagonal printing of matrix is ")
diagonalOrder(M)