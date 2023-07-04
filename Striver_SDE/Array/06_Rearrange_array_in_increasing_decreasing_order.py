'''
Problem Statement: Rearrange the array such that the first half is arranged in increasing order, and the second half is arranged in decreasing order

Examples:

Example 1:
Input: 8 7 1 6 5 9
Output: 1 5 6 9 8 7
Explanation: First three elements are in the ascending order and next three elements are in the descending order.

Example 2:
Input: 4 2 8 6 15 5 9 20
Output: 2 4 5 6 20 15 9 8
'''

arr = []
n = int(input("Enter the length of array: "))

for i in range(0,n):
    element = int(input("Enter the value: "))
    arr.append(element)
    
arr.sort()
for i in range(n // 2):
    print(arr[i], end=" ")
for i in range(n - 1, n // 2 - 1, -1):
    print(arr[i], end=" ")
