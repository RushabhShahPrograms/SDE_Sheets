'''
Write a program that take a user inputr of three angles and will
find out whether it can form a triangle or not
'''
def valid_triangle(a,b,c):
    if (a+b+c) == 180 and a != 0 and b != 0 and c != 0:
        return True
    else:
        return False
    
try:
    a = float(input("Enter angle a:"))
    b = float(input("Enter angle b:"))
    c = float(input("Enter angle c:"))

    if valid_triangle(a,b,c):
        print("Triangle is valid")
    else:
        print("Triangle is not valid")
except ValueError:
    print("Please enter valid angle values")