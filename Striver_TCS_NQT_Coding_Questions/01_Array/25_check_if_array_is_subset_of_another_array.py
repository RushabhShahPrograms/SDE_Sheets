'''
Write a program to find whether an array is a subset of another array or not.

Given arr1[] and arr2[], we need to find whether arr1[] is a subset of arr2[]. An array is called a subset of another if all of its elements are present in the other array.

Note: Array elements are assumed to be unique.

Examples:

Example 1:
Input: arr1[]= [1,3,4,5,2]
       arr2[]= [2,4,3,1,7,5,15]
Output: arr1[] is a subset of arr2[]

Example 2:
Input: arr1[]= [1,3,4,5,2]
       arr2[]= [4,5,2]
Output: arr1[] is not a subset of arr2[]

Example 3:
Input: arr1[]= [1,3,4,5,2]
       arr2[]= [11,12,13,15,16]
Output: arr1[] is not a subset of arr2[]
'''

def isSubset(arr1, m, arr2, n):
    if m > n:
        return False
    for i in range(m):
        present = False
        for j in range(n):
            if arr2[j] == arr1[i]:
                present = True
                break
        if present == False:
            return False
    return True

arr1 = [1, 3, 4, 5, 2]
arr2 = [2, 4, 3, 1, 7, 5, 15]
m = len(arr1)
n = len(arr2)
ans = isSubset(arr1, m, arr2, n)
if ans == True:
    print("arr1[] is a subset of arr2[]")
else:
    print("arr1[] is not a subset of arr2[]")
