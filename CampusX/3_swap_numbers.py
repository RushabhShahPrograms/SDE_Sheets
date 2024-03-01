'''
User will input (2numbers).Write a program to swap the numbers
'''
a = int(input("Enter a"))
b = int(input("Enter b"))

def swap(a,b):
    t = a
    a = b
    b = t
    return a,b

a,b = swap(a,b)
print("a",a,"b",b)