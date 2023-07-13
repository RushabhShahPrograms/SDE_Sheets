'''
Problem:  Given an array of size n, sort the array using Merge Sort.

Examples:

Example 1:
Input: N=5, arr[]={4,2,1,6,7}
Output: 1,2,4,6,7,


Example 2:
Input: N=7,arr[]={3,2,8,5,1,4,23}
Output: 1,2,3,4,5,8,23
'''

def merge(arr, low, mid, high):
    temp = []  # temporary array
    left = low  # starting index of left half of arr
    right = mid + 1  # starting index of right half of arr

    # storing elements in the temporary array in a sorted manner

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # if elements on the left half are still left

    while left <= mid:
        temp.append(arr[left])
        left += 1

    # if elements on the right half are still left
    while right <= high:
        temp.append(arr[right])
        right += 1

    # transferring all elements from temporary to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def mergeSort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergeSort(arr, low, mid)  # left half
    mergeSort(arr, mid + 1, high)  # right half
    merge(arr, low, mid, high)  # merging sorted halves



#Driver Code
n = int(input("Enter the size of the array: "))
arr = input("Enter multiple values separated by space: ").split()
arr = [int(i) for i in arr[0:n]]

print("Before Sorting Array: ")
for i in range(0, n):
    print(arr[i], end=" ")
print()

mergeSort(arr, 0, n - 1)

print("After Sorting Array: ")
for i in range(0, n):
    print(arr[i], end=" ")
print()
