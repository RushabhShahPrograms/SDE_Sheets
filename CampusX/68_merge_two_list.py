'''
Write a program to merge 2 list without using the + operator
'''

def merge_list(list1,list2):
    list1.extend(list2)
    return list1

print(merge_list([1,2,3],[4,5,6]))