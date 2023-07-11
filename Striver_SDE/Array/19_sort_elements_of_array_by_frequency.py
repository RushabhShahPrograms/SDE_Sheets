'''
Problem Statement: Given an array of integers, having some duplicate elements, sort the array by frequency.

Examples:

Example 1:
Input: N = 8, array[] = {1,2,3,2,4,3,1,2}
Output: 2 2 2 1 1 3 3 4 
Explanation: Since  2 is present 3 times in an array , so print it 3 times ,then print ‘1’ 2 times and then ‘3’ 2 times and 4 has least frequency, it will be printed at last.

Example 2:
Input: N = 6, array[] = {-199,6,7,-199,3,5}
Output: -199 -199 3 5 6 7
Explanation: Since -199 is present 2 times so it will be printed at first , then 3 , 5 ,6 ,7 are present once in array , so print them in their sorted order.
'''

def sort2darray(array2d, k):
    for i in range(k - 1):
        for j in range(k - 1 - i):
            if array2d[1][j] < array2d[1][j + 1]:
                array2d[1][j], array2d[1][j + 1] = array2d[1][j + 1], array2d[1][j]
                array2d[0][j], array2d[0][j + 1] = array2d[0][j + 1], array2d[0][j]

def Sortele(arr, n):
    arr.sort()
    arr2d = [[0 for i in range(100)] for j in range(2)]
    k = 0
    count = 0
    for i in range(n):
        if i == 0:
            arr2d[0][k] = arr[i]
            count = 1
        elif arr[i] == arr[i - 1]:
            count += 1
        else:
            arr2d[1][k] = count
            count = 1
            k += 1
            arr2d[0][k] = arr[i]
    arr2d[1][k] = count
    k += 1
    sort2darray(arr2d, k)
    k = 0
    i = 0
    while i < n:
        while arr2d[1][k] > 0:
            arr[i] = arr2d[0][k]
            i += 1
            arr2d[1][k] -= 1
        k += 1

n = 8
arr = [1, 2, 3, 2, 4, 3, 1, 2]
Sortele(arr, n)
for i in range(n):
    print(arr[i], end=" ")