'''
Write a program that can create a new list from a given list where each item in the new list is square of the item of the old list
'''

def square_list(lst):
    return [item**2 for item in lst]

print(square_list([1,2,3,4,5]))