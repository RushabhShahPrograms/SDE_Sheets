'''
Problem Statement: Given an array, we have to find the sum of all the elements in the array.

Examples:

Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: 15
Explanation: Sum of all the elements is 1+2+3+4+5 = 15

Example 2:
Input:  N=6, array[] = {1,2,1,1,5,1}
Output: 11
Explanation: Sum of all the elements is 1+2+1+1+5+1 = 11
'''

arr = []
sum = 0
n = int(input("Enter the length of array: "))

for i in range(0,n):
    element = int(input("Enter the value: "))
    arr.append(element)
    
for i in range(n):
    sum += arr[i]
    
print("Sum is: ",sum)
