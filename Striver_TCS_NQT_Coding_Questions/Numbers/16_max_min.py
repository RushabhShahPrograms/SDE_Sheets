'''
Problem Statement: Given a number N, print the smallest and largest digits present in the number.

Examples:

Example 1:
Input: N = 2746
Output: Largest digit: 7
        Smallest digit: 2
Explanation: By simply going through the digits of 
the number, we figure out the largest and smallest 
digit in the number.

Example 2:
Input: N = 23004
Output: Largest digit : 4
        Smallest digit : 0
Explanation: By simply going through the digits of 
the number, we figure out the largest and smallest 
digit in the number.
'''

def MinMax(n):
    mini = 9**9
    maxi = -9**9
    while n != 0:
        d = n % 10
        mini = min(mini,d)
        maxi = max(maxi,d)
        n //= 10
    
    print("The minimum number is:", mini)
    print("The maximum number is:", maxi)

n = int(input("Enter the number: "))
MinMax(n)


