'''
Problem Statement: Given an array of pairs, find all the symmetric pairs in the array.

Examples:

Example 1:
Input: (1,2),(2,1),(3,4),(4,5),(5,4)
Output: (2,1) (5,4)
Explanation: Since (1,2) and (2,1) are symmetric pairs and (4,5) and (5,4) are symmetric pairs.

Example 2:
Input: (1,5),(2,3),(4,2),(5,1),(2,4)
Output: (2,4) (5,1)
Explanation: Since (1,5) and (2,4) are symmetric pairs and (5,1) and (4,2) are symmetric pairs.
'''

n = 5
arr = [[1, 2], [2, 1], [3, 4], [4, 5], [5, 4]]
mp = {}
print("The Symmetric Pairs are:")
for i in range(n):
    first = arr[i][0]
    second = arr[i][1]

    # if {second,first} existed previously, print them
    if second in mp and mp[second] == first:
        print(f"({first} {second})", end=" ")

    # else store them in the map
    else:
        mp[first] = second