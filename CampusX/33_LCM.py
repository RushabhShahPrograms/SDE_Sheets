'''
User will provide 2 numbers you have to find the by LCM of those 2 numbers
'''

def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x

def lcm(x,y):
    return (x*y)//gcd(x,y)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = lcm(num1,num2)

print(f"The LCM of {num1} and {num2} is {result}")