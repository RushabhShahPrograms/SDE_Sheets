'''
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
'''

n = int(input("Enter a number: "))
n_str = str(n)
result = n + int(n_str*2) + int(n_str*3)
print(f"The result of {n}+{n_str*2} + {n_str*3} is {result}")