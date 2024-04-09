'''
Given a matrix of ‘O’ and ‘X’, replace ‘O’ with ‘X’ if surrounded by ‘X’
Last Updated : 20 Oct, 2023
Given a matrix where every element is either ‘O’ or ‘X’, replace ‘O’ with ‘X’ if surrounded by ‘X’. A ‘O’ (or a set of ‘O’) is considered to be surrounded by ‘X’ if there are ‘X’ at locations just below, just above, just left, and just right of it. 

Examples: 

Input: mat[M][N] = {{‘X’, ‘O’, ‘X’, ‘X’, ‘X’, ‘X’},
{‘X’, ‘O’, ‘X’, ‘X’, ‘O’, ‘X’},
{‘X’, ‘X’, ‘X’, ‘O’, ‘O’, ‘X’},
{‘O’, ‘X’, ‘X’, ‘X’, ‘X’, ‘X’},
{‘X’, ‘X’, ‘X’, ‘O’, ‘X’, ‘O’},
{‘O’, ‘O’, ‘X’, ‘O’, ‘O’, ‘O’}};

Output: mat[M][N] = {{‘X’, ‘O’, ‘X’, ‘X’, ‘X’, ‘X’},
{‘X’, ‘O’, ‘X’, ‘X’, ‘X’, ‘X’},
{‘X’, ‘X’, ‘X’, ‘X’, ‘X’, ‘X’},
{‘O’, ‘X’, ‘X’, ‘X’, ‘X’, ‘X’},
{‘X’, ‘X’, ‘X’, ‘O’, ‘X’, ‘O’},
{‘O’, ‘O’, ‘X’, ‘O’, ‘O’, ‘O’}};

Input: mat[M][N] = {{‘X’, ‘X’, ‘X’, ‘X’}
{‘X’, ‘O’, ‘X’, ‘X’}
{‘X’, ‘O’, ‘O’, ‘X’}
{‘X’, ‘O’, ‘X’, ‘X’}
{‘X’, ‘X’, ‘O’, ‘O’} };

Output: mat[M][N] = {{‘X’, ‘X’, ‘X’, ‘X’}
{‘X’, ‘X’, ‘X’, ‘X’}
{‘X’, ‘X’, ‘X’, ‘X’}
{‘X’, ‘X’, ‘X’, ‘X’}
{‘X’, ‘X’, ‘O’, ‘O’}};
'''

M = 6
N = 6

def floodFillUtil(mat,x,y,prevV,newV):
    if(x<0 or x>=M or y<0 or y>=N):
        return
    if(mat[x][y]!=prevV):
        return
    
    mat[x][y] = newV

    floodFillUtil(mat,x+1,y,prevV,newV)
    floodFillUtil(mat,x-1,y,prevV,newV)
    floodFillUtil(mat,x,y+1,prevV,newV)
    floodFillUtil(mat,x,y-1,prevV,newV)

def replaceSurrounded(mat):
    for i in range(M):
        for j in range(N):
            if(mat[i][j] == 'O'):
                mat[i][j] = '-'

        for i in range(M):
            if (mat[i][0] == '-'):
                floodFillUtil(mat, i, 0, '-', 'O')
     
    # Right side
    for i in range(M): 
        if (mat[i][N - 1] == '-'):
            floodFillUtil(mat, i, N - 1, '-', 'O')
     
    # Top side
    for i in range(N): 
        if (mat[0][i] == '-'):
            floodFillUtil(mat, 0, i, '-', 'O')
     
    # Bottom side
    for i in range(N): 
        if (mat[M - 1][i] == '-'):
            floodFillUtil(mat, M - 1, i, '-', 'O')
 
    # Step 3: Replace all '-' with 'X'
    for i in range(M):
        for j in range(N):
            if (mat[i][j] == '-'):
                mat[i][j] = 'X'

if __name__ == '__main__':
 
    mat = [ [ 'X', 'O', 'X', 'O', 'X', 'X' ], 
            [ 'X', 'O', 'X', 'X', 'O', 'X' ], 
            [ 'X', 'X', 'X', 'O', 'X', 'X' ], 
            [ 'O', 'X', 'X', 'X', 'X', 'X' ], 
            [ 'X', 'X', 'X', 'O', 'X', 'O' ], 
            [ 'O', 'O', 'X', 'O', 'O', 'O' ] ]; 
 
    replaceSurrounded(mat)
 
    for i in range(M):
        print(*mat[i])