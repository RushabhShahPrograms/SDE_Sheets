'''
Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons.

Input: arr[] = {3, 5, 4, 1, 9}
Output: Minimum element is: 1
        Maximum element is: 9

Input: arr[] = {22, 14, 8, 17, 35, 3}
Output:  Minimum element is: 3
         Maximum element is: 35
'''

def getMinMax(arr):
    arr.sort()
    minmax = {"min":arr[0], "max":arr[-1]}
    return minmax

arr = [12,45,890,34,56,678,1]
minmax = getMinMax(arr)

print("Minimum element is: ",minmax["min"])
print("Maximum element is: ",minmax["max"])