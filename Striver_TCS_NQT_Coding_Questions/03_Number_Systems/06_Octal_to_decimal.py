'''
Problem Statement: Given an Octal Number, convert it into a Decimal Number.

In Octal to Decimal Conversion, We will take every digit of the number and multiply it with 8 raised to power i  which will increase by 1 when we move to the next digit and then add it to sum. This task is repeated until n becomes 0. 

Examples:

Example 1:
Input: 345
Output: 229
Explanation: Decimal equivalent of given Octal expressionis 229

Example 2:
Input: 170
Output: 121
Explanation: Decimal equivalent of given Octal expression is121
'''

def OctaltoDecimal(Octal):
     Decimal = i = 0
     while(Octal!=0):
        rem = Octal % 10
        Decimal += rem*pow(8,i)
        i+=1
        Octal //=10
     return Decimal 

#Driver Code
Octal = int(input("Enter the number in Octal value: "))
print("The decimal equivalent of the given octal represent is",OctaltoDecimal(Octal))