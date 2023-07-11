'''
Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

Examples:

Example 1:
Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
Output: 6 7 1 2 3 4 5
Explanation: array is rotated to right by 2 position .

Example 2:
Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left 
Output: 9 10 11 3 7 8
Explanation: Array is rotated to right by 3 position.
'''

def Reverse(arr,start,end):
    while start<=end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

def Rotateeletoleft(arr,n,k):
    Reverse(arr,0,k-1)
    Reverse(arr,k,n-1)
    Reverse(arr,0,n-1)

arr = [1,2,3,4,5,6,7]
n = len(arr)
k = 2
Rotateeletoleft(arr,n,k)
print("After Rotating the k elements to left ", end="")
for i in range(n):
    print(arr[i], end=" ")
print()