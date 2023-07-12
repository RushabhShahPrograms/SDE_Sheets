'''
Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.

Examples:

Example 1:
Input: N = 5
Output: 0 1 1 2 3 5
Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

Example 2:
Input: 6

Output: 0 1 1 2 3 5 8
Explanation: 0 1 1 2 3 5 8 is the fibonacci series upto 6th term.(o based indexing)
'''

n = int(input("Enter the number: "))
if n == 0:
    print("The Fibonacci Series up to", n, "th term:")
    print(0)
else:
    secondLast = 0 #for (i-2)th term
    last = 1 #for (i-1)th term
    print("The Fibonacci Series up to", n, "th term:")
    print(secondLast, last, end=" ")
    for i in range(2,n+1):
        cur = last + secondLast
        secondLast = last
        last = cur
        print(cur, end=" ")