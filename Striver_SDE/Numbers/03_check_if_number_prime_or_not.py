'''
Problem Statement: Given a number, check whether it is prime or not. A prime number is a natural number that is only divisible by 1 and by itself.

Examples 1 2 3 5 7 11 13 17 19 …

Examples
Example 1:
Input: N = 3
Output: Prime
Explanation: 3 is a prime number

Example 2:
Input: N = 26
Output: Non-Prime
Explanation: 26 is not prime
'''

def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

n = 11
ans = isPrime(n)
if n!=1 and ans == True:
    print("Prime Number")
else:
    print("Not Prime")