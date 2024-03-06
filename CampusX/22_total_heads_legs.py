'''
Write a program that will tell the number of dogs and chicken are
there when the user will provide the value of total heads and legs.
'''

def solve(heads, legs):
    d = legs/2 - heads
    c = heads - d
    return d, c

heads = int(input("Enter the total number of heads: "))
legs = int(input("Enter the total number of legs: "))

d, c = solve(heads,legs)
if d<0 or c<0 or not d.is_integer() or not c.is_integer():
    print("Invalid input")
else:
    print(f"There are {int(d)} dogs and {int(c)} chickens.")