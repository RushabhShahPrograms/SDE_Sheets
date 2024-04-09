'''
Write a code which inputs two numbers m and n and creates a matrix of size m x n (m rows and n columns) in which every elements is either X or 0. The Xs and 0s must be filled alternatively, the matrix should have outermost rectangle of Xs, then a rectangle of 0s, then a rectangle of Xs, and so on.

Examples:  

Input: m = 3, n = 3
Output: Following matrix 
X X X
X 0 X
X X X

Input: m = 4, n = 5
Output: Following matrix
X X X X X
X 0 0 0 X
X 0 0 0 X
X X X X X

Input:  m = 5, n = 5
Output: Following matrix
X X X X X
X 0 0 0 X
X 0 X 0 X
X 0 0 0 X
X X X X X

Input:  m = 6, n = 7
Output: Following matrix
X X X X X X X
X 0 0 0 0 0 X
X 0 X X X 0 X
X 0 X X X 0 X
X 0 0 0 0 0 X
X X X X X X X 
'''

def fill0X(m,n):
    i,k,l = 0,0,0
    r=m
    c=n
    a=[[None]*n  for i in range(m)]
    x = 'X'

    while k<m and l<n:
        for i in range(l,n):
            a[k][i]=x
        k += 1

        for i in range(k,m):
            a[i][n-1]=x
        n -= 1

        if k<m:
            for i in range(n-1,l-1,-1):
                a[m-1][i]=x
            m -= 1
        
        if l<n:
            for i in range(m-1,k-1,-1):
                a[i][l] = x
            l += 1
        
        x = 'X' if x == 'O' else 'O'

    for i in range(r):
        for j in range(c):
            print(a[i][j],end=" ")
        print()

print("Output for m = 5, n = 6") 
fill0X(5, 6) 
 
print("Output for m = 4, n = 4") 
fill0X(4, 4) 
 
print("Output for m = 3, n = 4") 
fill0X(3, 4)