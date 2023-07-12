'''
Problem Statement: Given an array of n size, rotate the array by k elements using the Block Swap Algorithm.

Examples:

Example 1:
Input: N = 5, array[] = {1,2,3,4,5} K=2
Output: {3,4,5,1,2}
Explanation: Rotate the array to right by 2 elements.

Example 2:
Input: N = 7, array[] = {1,2,3,4,5,6,7} K=3
Output: {4,5,6,7,1,2,3}
Explanation: Rotate the array to right by 3 elements.
'''

def swap(arr, a, b, k):
    for i in range(k):
        temp = arr[a + i]
        arr[a + i] = arr[b + i]
        arr[b + i] = temp

def BlockSwap(arr, k, n):
    if k == 0 or k == n:
        return
    if k == n - k:
        swap(arr, 0, n - k, k)
        return
    elif k < n - k:
        swap(arr, 0, n - k, k)
        BlockSwap(arr, k, n - k)
    else:
        swap(arr, 0, k, n - k)
        BlockSwap(arr[n - k:], 2 * k - n, k)

arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
k = 2
BlockSwap(arr, k, n)
print("After Rotating the array ")
for i in range(n):
    print(arr[i], end=" ")
