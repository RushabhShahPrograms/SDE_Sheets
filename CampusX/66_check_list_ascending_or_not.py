'''
Write a program to check if a list is in ascending order or not
'''

def is_ascending(lst):
    return lst == sorted(lst)

print(is_ascending([1,2,3,4,5,6]))
print(is_ascending([5,4,3,2,1]))