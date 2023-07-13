'''
Problem Statement: 

Remove brackets from an algebraic expression

Write a program to remove brackets from an algebraic expression

Given an algebraic expression, we need to simplify the expression and remove the brackets.

Examples:

Example 1:
Input: “a+((b-c)+d)”
Output: “a+b-c+d”
Explanation: Removed all the brackets in the algebric expression.

Example 2:
Input: “(((a-b))+c)”
Output: “a-b+c”
Explanation: Removed all the brackets in the algebric expression.
'''

def solve(inp):
    answer = ""
    for i in inp:
        if i != '(' and i != ')':
            answer += i
    return answer

input1 = "a+((b-c)+d)"
input2 = "(((a-b))+c)"

print("Original String: ", input1)
print("After removing brackets: ", solve(input1))
print("Original String: ", input2)
print("After removing brackets: ", solve(input2))
