'''
Write a program to print all the unique combinations of 1,2,3 and 4
'''

import itertools

numbers = [1,2,3,4]

for r in range(1,len(numbers)+1):
    for combination in itertools.combinations(numbers,r):
        print(combination)