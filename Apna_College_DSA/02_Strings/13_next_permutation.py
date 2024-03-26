'''
Implement the next permutation, which rearranges the list of numbers into Lexicographically next greater permutation of list of numbers. If such arrangement is not possible, it must be rearranged to the lowest possible order i.e. sorted in an ascending order. You are given an list of numbers arr[ ] of size N.

Example 1:

Input: N = 6
arr = {1, 2, 3, 6, 5, 4}
Output: {1, 2, 4, 3, 5, 6}
Explaination: The next permutation of the 
given array is {1, 2, 4, 3, 5, 6}.
Example 2:

Input: N = 3
arr = {3, 2, 1}
Output: {1, 2, 3}
Explaination: As arr[] is the last 
permutation. So, the next permutation 
is the lowest one.
Your Task:
You do not need to read input or print anything. Your task is to complete the function nextPermutation() which takes N and arr[ ] as input parameters and returns a list of numbers containing the next permutation.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 10000
'''

def nextPermutation(N,arr):
    for i in range(N-2, -1, -1):
        if arr[i]<arr[i+1]:
            break
    else:
        return sorted(arr)
    
    for j in range(N-1,i,-1):
        if arr[j]>arr[i]:
            arr[i],arr[j] = arr[j],arr[i]
            break
    
    arr[i+1:] = reversed(arr[i+1:])
    return arr

print(nextPermutation(6,[1,2,3,6,5,4]))
print(nextPermutation(3,[3,2,1]))