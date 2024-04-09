'''
Given a matrix where every row is sorted in increasing order. Write a function that finds and returns a common element in all rows. If there is no common element, then returns -1. 
Example: 
 

Input: mat[4][5] = { {1, 2, 3, 4, 5},
                    {2, 4, 5, 8, 10},
                    {3, 5, 7, 9, 11},
                    {1, 3, 5, 7, 9},
                  };
Output: 5
'''

M = 4
N = 5

def findCommon(mat):
    column = [N-1]*M
    min_row = 0

    while(column[min_row]>=0):
        for i in range(M):
            if(mat[i][column[i]]<mat[min_row][column[min_row]]):
                min_row = i
        
        eq_count = 0

        for i in range(M):
            if(mat[i][column[i]]>mat[min_row][column[min_row]]):
                if(column[i]==0):
                    return -1
                
                column[i] -= 1
            else:
                eq_count += 1
        
        if(eq_count == M):
            return mat[min_row][column[min_row]]
    return -1

if __name__ == "__main__": 
      
    mat = [[1, 2, 3, 4, 5], 
           [2, 4, 5, 8, 10], 
           [3, 5, 7, 9, 11], 
           [1, 3, 5, 7, 9]] 
  
    result = findCommon(mat) 
    if (result == -1): 
        print("No common element") 
    else: 
        print("Common element is", result)