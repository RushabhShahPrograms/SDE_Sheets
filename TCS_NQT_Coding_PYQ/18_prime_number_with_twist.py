'''
Write a code to check whether no is prime or not. Condition use function check() to find whether entered no is positive or negative ,if negative then enter the no, And if yes pas no as a parameter to prime() and check whether no is prime or not?

Whether the number is positive or not, if it is negative then print the message “please enter the positive number”
It is positive then call the function prime and check whether the take positive number is prime or not. 
'''

def prime(n):
    c = 0
    for i in range(2, n):
        if n % i == 0:
            c += 1
    if c >= 1:
        print(f"{n} is not a prime number")
    else:
        print(f"{n} is a prime number")

n = int(input("Enter no : "))
if n < 0:
    print("Please enter a positive integer")
else:
    prime(n)