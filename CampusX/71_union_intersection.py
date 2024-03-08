'''
Write a program that can perform union and intersection on 2 given list.
'''

def list_operations(list1,list2):
    union_result = list(set(list1) | set(list2))
    intersection_result = list(set(list1) & set(list2))
    
    return union_result, intersection_result

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

union, intersection = list_operations(list1, list2)

print("Union: ", union)
print("Intersection: ", intersection)