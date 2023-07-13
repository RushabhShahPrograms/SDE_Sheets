'''
Problem Statement: Given an array of N integers, write a program to implement the Selection sorting algorithm.

Examples:

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

Example 2:
Input: N=5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting the array is: 1, 2, 3, 4, 5
'''

def selection_sort(arr, n):
    # selection sort
    for i in range(0, n - 1):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        temp = arr[mini]
        arr[mini] = arr[i]
        arr[i] = temp

    print("After selection sort: ")
    for i in range(0, n):
        print(arr[i], end=" ")
    print()

#Driver Code
n = int(input("Enter the size of the array: "))
arr = input("Enter multiple values separated by space: ").split()
arr = [int(i) for i in arr[0:n]]

print("Before selection sort: ")
for i in range(0, n):
    print(arr[i], end=" ")
print()

selection_sort(arr, n)
