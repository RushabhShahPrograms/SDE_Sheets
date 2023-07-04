'''
Problem Statement: Given an array, we have to find the largest element in the array.

Examples
Example 1:
Input: arr[] = {2,5,1,3,0};
Output: 5
Explanation: 5 is the largest element in the array. 

Example 2: 
Input: arr[] = {8,10,5,7,9};
Output: 10
Explanation: 10 is the largest element in the array. 
'''

def LargestElement(arr):
    return max(arr)

arr = []
n = int(input("Enter length of the array: "))
for i in range(0, n):
    element = int(input("Enter the value: "))
    arr.append(element)

max = LargestElement(arr)
print("The largest element in the array is:", max)
