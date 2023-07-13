'''
Problem Statement: Given an integer Print “YES” if it is a strong number else print “NO”.

Note : 

When the sum of factorial of individual digits of a number is equal to the original number the number is called a strong number. 
Strong number is also known as Krishnamurthi number/Peterson Number.
Examples:

Examples 1:
Input: N = 145
Output: Yes
Explanation: 1! + 4! + 5! = 145. Hence 145 is a strong number. 

Example 2:
Input:  26
Output: No
Explanation: 2! + 6! = 722. Hence 26 is not a strong number.
'''

# Function to calculate the factorial of the individual digits
def Factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

# Function to compute sum of factorials
def Strong_No(num):
    sum = 0
    # Extract all the digits from num
    while num > 0:
        digit = num % 10
        sum = sum + Factorial(digit)
        num //= 10
    return sum

number = int(input("Enter the value: ")) #try 145 and 153
answer = Strong_No(number)
if answer == number and number != 0:
    print("YES")
else:
    print("NO")