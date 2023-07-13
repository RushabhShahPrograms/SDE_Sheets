'''
Problem Statement: Given an Octal Number, convert it into Binary Number.

For Decimal to Binary Conversion, we will divide the given number by 2 ( Since the Binary Numbers System has 2 digits in use ) repeatedly, and its remains will be stored till the number becomes zero.

Examples:

Example 1:
Input: 345
Output: 011100101
Explanation: Binary equivalent of given Octal expressionis 011100101

Example 2:
Input: 170
Output: 001111000
Explanation: Binary equivalent of given Octal expression is 001111000
'''

def OctaltoDecimal(Octal):
    Decimal = i = 0
    while(Octal!=0):
        rem = Octal%10
        Decimal += rem * pow(8,i)
        i+=1
        Octal //= 10
    return Decimal

def DecimaltoBinary(decimal):
    Binary = i =0
    while(decimal!=0):
        rem = decimal%2
        Binary += (rem*pow(10,i))
        i+=1
        decimal //= 2
    return Binary

#Driver Code
Octal = int(input("Enter the number in Octal form: "))
Decimal = OctaltoDecimal(Octal)
print("The binary conversion of the given octal number is",DecimaltoBinary(Decimal))