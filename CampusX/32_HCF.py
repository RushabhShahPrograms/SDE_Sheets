'''
User will provide 2 numbers you have to find the HCF of those 2 numbers
'''

def hcf(x,y):
    while(y):
        x,y=y,x%y
    return x

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = hcf(num1,num2)
print(f"The HCF of {num1} and {num2} is {result}")
