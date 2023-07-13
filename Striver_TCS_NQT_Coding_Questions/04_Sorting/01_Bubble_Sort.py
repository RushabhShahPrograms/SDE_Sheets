'''
Problem Statement: Given an array of N integers, write a program to implement the Bubble Sorting algorithm.

Examples:

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting we get 9,13,20,24,46,52


Input: N = 5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting we get 1,2,3,4,5
'''

def bubble_sort(arr, n):
    # bubble sort
    for i in range(n - 1, -1, -1):
        didSwap = 0
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
                didSwap = 1
        if didSwap == 0:
            break

    print("After Using bubble sort: ")
    for i in range(0, n):
        print(arr[i], end=" ")
    print()

#Driver Code
arr = []
n = int(input("Enter size of the array: "))
for i in range(0, n):
    element = int(input("Enter the value: "))
    arr.append(element)

print("Before Using Bubble Sort: ")
for i in range(0, n):
    print(arr[i], end=" ")
print()

bubble_sort(arr, n)
