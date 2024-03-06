'''
Write a program to find the sum of first n numbers, where n will be provided by the user. Eg if the user provides n=10 the output should be 55
'''

n = int(input("Enter a number: "))
sum_n = n * (n+1)//2

print(f"The sum of the first {n} numbers is {sum_n}")