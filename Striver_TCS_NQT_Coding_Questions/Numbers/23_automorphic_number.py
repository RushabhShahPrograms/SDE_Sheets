'''
Problem Statement: Given a number, check if it is automorphic or not. A number is called an Automorphic number if and only if its square ends in the same digits as the number itself.

Examples:

Example 1:
Input Format: N = 76
Result: Automorphic Number
Explanation: Calculating 76 * 76 gives 5776, it ends with the given number.

Input Format: 25
Result: Automorphic Number
Explanation: Calculating 25 * 25 gives 625, it ends with the given number.
'''

def isAutomorphic(N):
    sq = N * N
    while N > 0:
        # Check if last digit is equal or not
        if N % 10 != sq % 10:
            return False
        # Reducing the number and its square
        N //= 10
        sq //= 10
    return True

N = 25
if isAutomorphic(N):
    print("Automorphic Number")
else:
    print("Not Automorphic Number")