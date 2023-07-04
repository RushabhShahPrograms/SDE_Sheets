'''
Problem Statement: Given an array, we have to find the smallest element in the array.

Examples:

Example 1:
Input: arr[] = {2,5,1,3,0};
Output: 0
Explanation: 0 is the smallest element in the array. 

Example2: 
Input: arr[] = {8,10,5,7,9};
Output: 5
Explanation: 5 is the smallest element in the array.
'''

def SmallestElement(arr):
    # min = arr[0]
    # for i in range(0, len(arr)):
    #     if (min > arr[i]):
    #         min = arr[i]
    return min(arr)

arr = []
n = int(input("Enter number of elements in the array: "))
for i in range(0, n):
    element = int(input())
    arr.append(element)

min = SmallestElement(arr)
print("The smallest element in the array is:", min)
