'''
Write a program that can convert a 2D list to 1D listWrite a program that
can print
'''

def flatten_list(lst):
    return[item for sublist in lst for item in sublist]

print(flatten_list([[1,2,3],[4,5,6],[7,8,9]]))