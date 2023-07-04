'''
Problem Statement: You are given an array. The task is to reverse the array and print it. 

Examples:

Example 1:
Input: N = 5, arr[] = {5,4,3,2,1}
Output: {1,2,3,4,5}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

Example 2:
Input: N=6 arr[] = {10,20,30,40}
Output: {40,30,20,10}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.
'''

def reverseArr(n,arr):
    return arr[::-1] # here '::' is used to slice the array and '-1' is used to reverse the order of the elements
    

#Main
arr = []
n = int(input("Enter length of the array: "))
for i in range(0, n):
    element = int(input("Enter the value: "))
    arr.append(element)

revarr = reverseArr(n,arr)
print("The reversed array is: ",revarr)
