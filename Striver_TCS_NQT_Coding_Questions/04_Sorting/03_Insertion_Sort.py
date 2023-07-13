'''
Problem Statement: Given an array of N integers, write a program to implement the Insertion sorting algorithm.

Examples:

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: 
After sorting the array is: 9,13,20,24,46,52


Example 2:
Input: N=5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting the array is: 1,2,3,4,5
'''

def insertion_sort(arr, n):
    for i in range(0, n - 1):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            temp = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = temp
            j -= 1

    print("After Using insertion sort: ")
    for i in range(0, n):
        print(arr[i], end=" ")
    print()

#Driver Code
n = int(input("Enter the size of the array: "))
arr = input("Enter multiple values separated by space: ").split()
arr = [int(i) for i in arr[0:n]]

print("Before Using insertion Sort: ")
for i in range(0, n):
    print(arr[i], end=" ")
print()

insertion_sort(arr, n)