'''
Problem Statement: Given an unsorted array, remove duplicates from the array.

Examples:

Example 1:
Input: arr[]={2,3,1,9,3,1,3,9}
Output:  {2,3,1,9}

Explanation: Removed all the duplicate elements

Example 2:
Input: arr[]={4,3,9,2,4,1,10,89,34}
Output: {3,4,9,2,1,10,34,89}
Explanation: Removed all the duplicate elements
'''

class removeDuplicates:
    def duplicate(self,arr):
        mark = [1]*len(arr)
        for i in range(len(arr)):
            if mark[i] == 1:
                for j in range(i+1,len(arr)):
                    if arr[i] == arr[j]:
                        mark[j] = 0
        
        for i in range(len(arr)):
            if mark[i] == 0:
                print(arr[i],end=",")

arr = [4,3,9,2,4,1,10,89,34]
d1 = removeDuplicates()
d1.duplicate(arr)