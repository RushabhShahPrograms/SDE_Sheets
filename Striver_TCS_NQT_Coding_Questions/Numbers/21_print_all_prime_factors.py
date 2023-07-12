'''
Problem Statement: Given a number n. Print all Prime Factors of the given number n.

Examples:

Example 1:
Input: N = 12
Output: 2,2,3
Explanation: These are the prime factors of 12.

Example 2:
Input: N = 36
Output: 2,2,3,3
Explanation: These are the prime factors of 36.
'''

class PrimeFactors:
    def printPrimeFactors(self, n):
        print("Prime Factors :", end=" ")
        for i in range(2, n+1):
            if n % i == 0:
                while n % i == 0:
                    print(i, end=" ")
                    n //= i

n = int(input("Enter the value: "))
p1 = PrimeFactors()
p1.printPrimeFactors(n)
