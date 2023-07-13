'''
Problem Statement: Given a decimal number, convert it into Octal Number.

Examples:

Example 1:
Input:  17
Output: 21
Explanation: Octal Equivalent of 17 is 21

Example 2:
Input:  45
Output: 55
Explanation: Octal Equivalent of 45 is 55
'''

def DecimaltoOctal(decimal):
    Octal = 0
    i = 0
    while(decimal!=0):
        rem = decimal%8
        Octal += rem*pow(10,i)
        i+=1
        decimal //= 8
    return Octal

#Driver Code
decimal = int(input("Enter the decimal value: "))
print("The Octal conversion of the given decimal number is ",DecimaltoOctal(decimal))