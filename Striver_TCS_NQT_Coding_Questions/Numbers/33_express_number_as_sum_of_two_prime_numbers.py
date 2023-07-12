'''
Problem: Given a number n, express the number as a sum of 2 prime numbers.

Examples:

Example 1:
Input : N = 74
Output : True . 
Explanation: 74 can be expressed as 71 + 3 and both are prime numbers. 

Example 2:
Input : N = 11
Output : False. 
Explanation: 11 cannot be expressed as sum of two prime numbers.
'''

class SumOf2Prime:
    def isPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def prime(self, n):
        if self.isPrime(n) and self.isPrime(n - 2):
            return True
        else:
            return False

n = 19
s1 = SumOf2Prime()
if s1.prime(n):
    print("Yes")
else:
    print("No")
