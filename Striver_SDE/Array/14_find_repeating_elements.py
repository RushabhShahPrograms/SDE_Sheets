'''
Problem Statement: Find all the repeating elements present in an array.

Examples:

Example 1:
Input: 
Arr[] = [1,1,2,3,4,4,5,2]
Output:
 1,2,4
Explanation:
 1,2 and 4 are the elements which are occurring more than once.

Example 2:
Input:
 Arr[] = [1,1,0]
Output:
 1
Explanation:
 Only 1 is occurring more than once in the given array.
'''

def find_repeating_elements(arr):
    arr.sort()
    repeating_elements = []
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            repeating_elements.append(arr[i])

    print("The repeating elements are:",end=" ")
    print(*repeating_elements)

if __name__ == '__main__':
    arr = [1,1,2,3,4,4,5,2]
    find_repeating_elements(arr)