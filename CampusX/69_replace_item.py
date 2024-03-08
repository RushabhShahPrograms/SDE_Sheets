'''
Write a program to replace an item with a different item if found in the list
'''

def replace_item(lst,old_item,new_item):
    return [new_item if item==old_item else item for item in lst]

print(replace_item([1,2,3,4,5],3,'three'))