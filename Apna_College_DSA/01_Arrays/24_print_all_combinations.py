'''
Print all combinations
Given an array of size n, generate and print all possible combinations of r elements in the array.

Example:

Input: arr=[1,2,3,4], r=2

Output: 1 2
1 3
1 4
2 3
2 4
3 4

Input: arr=[1,2,3,4], r=3

Output: 1 2 3
1 2 4
1 3 4
2 3 4
'''

from itertools import combinations
def print_combinations(arr,r):
    comb = combinations(arr,r)

    for i in list(comb):
        print(' '.join(map(str,i)))

print_combinations([1,2,3,4],2)
print_combinations([1,2,3,4],3)