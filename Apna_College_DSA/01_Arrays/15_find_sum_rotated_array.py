'''
Find if there is a pair with a given sum in the rotated sorted Array
Given an array arr[] of distinct elements size N that is sorted and then rotated around an unknown point, the task is to check if the array has a pair with a given sum X.

Examples : 

Input: arr[] = {11, 15, 6, 8, 9, 10}, X = 16
Output: true
Explanation: There is a pair (6, 10) with sum 16

Input: arr[] = {11, 15, 26, 38, 9, 10}, X = 35
Output: true
Explanation: There is a pair (26, 9) with sum 35

Input: arr[] = {11, 15, 26, 38, 9, 10}, X = 45
Output: false
Explanation: There is no pair with sum 45.
'''

def pairInSortedRotated(arr,n,x):
    for i in range(0,n):
        if(arr[i]>arr[i+1]):
            break;

    l = (i+1)%n
    r=i

    while(l!=r):
        if(arr[l] + arr[r] == x):
            return True
        if(arr[l]+arr[r]<x):
            l = (l+1)%n
        else:
            r = (n+r-1)%n
    return False

print(pairInSortedRotated([11, 15, 6, 8, 9, 10], 6, 16))
print(pairInSortedRotated([11, 15, 26, 38, 9, 10], 6, 35))
print(pairInSortedRotated([11, 15, 26, 38, 9, 10], 6, 45))