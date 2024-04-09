'''
Given a binary matrix, find the maximum size rectangle binary-sub-matrix with all 1’s. 

Example: 

Input:
0 1 1 0
1 1 1 1
1 1 1 1
1 1 0 0
Output :
8
Explanation : 
The largest rectangle with only 1's is from 
(1, 0) to (2, 3) which is
1 1 1 1
1 1 1 1 

Input:
0 1 1
1 1 1
0 1 1      
Output:
6
Explanation : 
The largest rectangle with only 1's is from 
(0, 1) to (2, 2) which is
1 1
1 1
1 1
Recommended Problem
Max rectangle
Dynamic Programming
Stack
+3 more
Flipkart
Amazon
+6 more
Solve Problem
Submission count: 98.8K
There is already an algorithm discussed a dynamic programming based solution for finding the largest square with 1s. 

Approach: 

In this post, an interesting method is discussed that uses largest rectangle under histogram as a subroutine. 

If the height of bars of the histogram is given then the largest area of the histogram can be found. This way in each row, the largest area of bars of the histogram can be found. To get the largest rectangle full of 1’s, update the next row with the previous row and find the largest area under the histogram, i.e. consider each 1’s as filled squares and 0’s with an empty square and consider each row as the base.

Illustration: 

Input :
0 1 1 0
1 1 1 1
1 1 1 1
1 1 0 0
Step 1: 
0 1 1 0  maximum area  = 2
Step 2:
row 1  1 2 2 1  area = 4, maximum area becomes 4
row 2  2 3 3 2  area = 8, maximum area becomes 8
row 3  3 4 0 0  area = 6, maximum area remains 8
Algorithm: 

Run a loop to traverse through the rows.
Now If the current row is not the first row then update the row as follows, if matrix[i][j] is not zero then matrix[i][j] = matrix[i-1][j] + matrix[i][j].
Find the maximum rectangular area under the histogram, consider the ith row as heights of bars of a histogram. This can be calculated as given in this article Largest Rectangular Area in a Histogram
Do the previous two steps for all rows and print the maximum area of all the rows.
'''

class Solution(): 
    def maxHist(self, row): 
        result = [] 
        top_val = 0
        max_area = 0
  
        area = 0
        i = 0
        while (i < len(row)): 
  
            if (len(result) == 0) or (row[result[-1]] <= row[i]): 
                result.append(i) 
                i += 1
            else: 
                top_val = row[result.pop()] 
                area = top_val * i 
  
                if (len(result)): 
                    area = top_val * (i - result[-1] - 1) 
                max_area = max(area, max_area) 
  
        while (len(result)): 
            top_val = row[result.pop()] 
            area = top_val * i 
            if (len(result)): 
                area = top_val * (i - result[-1] - 1) 
  
            max_area = max(area, max_area) 
  
        return max_area 
  
    def maxRectangle(self, A): 

        result = self.maxHist(A[0]) 
  
        for i in range(1, len(A)): 
  
            for j in range(len(A[i])): 
  
                if (A[i][j]): 
                    A[i][j] += A[i - 1][j] 
  
            result = max(result, self.maxHist(A[i])) 
  
        return result 
  
  
# Driver Code 
if __name__ == '__main__': 
    A = [[0, 1, 1, 0], 
         [1, 1, 1, 1], 
         [1, 1, 1, 1], 
         [1, 1, 0, 0]] 
    ans = Solution() 
  
    print("Area of maximum rectangle is", 
          ans.maxRectangle(A))