'''
Write a python program to search a given number from a list
'''

def search_number(lst,num):
    if num in lst:
        return f"The number {num} is in list"
    else:
        return f"The number {num} is not in the list"
    
print(search_number([1,2,3,4,5,6,7,8],5))