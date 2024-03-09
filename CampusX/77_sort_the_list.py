'''
Write a program that can sort a given unsorted list. Dont use any built in function for sorting.
'''

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0,n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1], lst[j]
    
    return lst

unsorted_lst = [64,45,89,12,34,17,85,35]
print(bubble_sort(unsorted_lst))