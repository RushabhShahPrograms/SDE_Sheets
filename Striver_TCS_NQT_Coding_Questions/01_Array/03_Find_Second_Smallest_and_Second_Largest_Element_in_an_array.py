'''
Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

Examples
Example 1:
Input: [1,2,4,7,7,5]
Output: Second Smallest : 2
	Second Largest : 5
Explanation: The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2

Example 2:
Input: [1]
Output: Second Smallest : -1
	Second Largest : -1
Explanation: Since there is only one element in the array, it is the largest and smallest element present in the array. There is no second largest or second smallest element present.
'''

def secondsmallest(n,arr):
    if(n<2):
        return -1
    small = float('inf')
    second_small = float('inf')
    for i in range(n):
        if(arr[i]<small):
            second_small = small
            small = arr[i]
        elif (arr[i]<second_small and arr[i] != small):
            second_small = arr[i]
    return second_small
    
def secondlargest(n,arr):
    if (n < 2):
        return -1
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if (arr[i] > large):
            second_large = large
            large = arr[i]
        elif (arr[i] > second_large and arr[i] != large):
            second_large = arr[i]
    return second_large

#Main
arr = []
n = int(input("Enter length of the array: "))
for i in range(0, n):
    element = int(input("Enter the value: "))
    arr.append(element)

Ss = secondsmallest(n,arr)
Sl = secondlargest(n,arr)
print("The second Smallest is: ",Ss)
print("The second Largest is: ",Sl)
