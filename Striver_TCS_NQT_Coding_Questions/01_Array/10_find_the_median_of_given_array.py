'''
Problem Statement: Given an unsorted array, find the median of the given array.

Examples:

Example 1:
Input: [2,4,1,3,5]
Output: 3

Example 2:
Input: [2,5,1,7]
Output: 3.5
'''

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element " + str(i+1) + ": ")))

arr.sort()
mid = len(arr)//2
res = (arr[mid]+arr[~mid]) / 2
print("Median of array is: ",str(res))