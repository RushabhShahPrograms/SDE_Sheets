'''
Write a python program to remove all the duplicates from a list
'''

def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1,2,2,3,4,5,6,7,5,4,4,5,8,9,10,11,12,11]))