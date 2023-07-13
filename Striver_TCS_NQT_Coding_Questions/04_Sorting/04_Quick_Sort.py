'''
Problem Statement:  Given an array of n integers, sort the array using the Quicksort method.

Examples:

Example 1:
Input:  N = 5  , Arr[] = {4,1,7,9,3}
Output: 1 3 4 7 9 

Explanation: After sorting the array becomes 1, 3, 4, 7, 9

Example 2:
Input: N = 8 , Arr[] = {4,6,2,5,7,9,1,3}
Output: 1 2 3 4 5 6 7 9
Explanation: After sorting the array becomes 1, 3, 4, 7, 9
'''

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1

        while arr[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def qs(arr, low, high):
    if low < high:
        pIndex = partition(arr, low, high)
        qs(arr, low, pIndex - 1)
        qs(arr, pIndex + 1, high)

def quickSort(arr):
    qs(arr, 0, len(arr) - 1)
    return arr

#Driver code
n = int(input("Enter the size of the array: "))
arr = input("Enter multiple values separated by space: ").split()
arr = [int(i) for i in arr[0:n]]

print("Before Using quick Sort: ")
for i in range(0, n):
    print(arr[i], end=" ")
print()

arr = quickSort(arr)
print("After Using quick sort: ")
for i in range(0, n):
    print(arr[i], end=" ")
print()
