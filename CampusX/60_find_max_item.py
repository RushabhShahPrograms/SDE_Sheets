'''
Write a python program to find the max item from a list without using the max function
'''

def find_max(lst):
    max_item = lst[0]
    for item in lst:
        if item > max_item:
            max_item = item
    return max_item

print(find_max([1,2,3,4,5,6,7,8,34,45,23]))