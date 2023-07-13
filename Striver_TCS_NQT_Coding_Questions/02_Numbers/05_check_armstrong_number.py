'''
Problem Statement: Given a number, check if it is Armstrong Number or Not.

Examples:

Example 1:
Input:153 
Output: Yes, it is an Armstrong Number
Explanation: 1^3 + 5^3 + 3^3 = 153

Input:170 
Output: No, it is not an Armstrong Number
Explanation: 1^3 + 7^3 + 0^3 != 170
'''

def ArmstrongNumber(n):
    originalno = n
    count = 0
    temp = n
    while temp != 0:
        count += 1
        temp //= 10
    sumofpower = 0
    while n != 0:
        digit = n % 10
        sumofpower += pow(digit, count)
        n //= 10
    return sumofpower == originalno




if __name__ == "__main__":
    n1 = 153
    if ArmstrongNumber(n1):
        print("Yes, it is an Armstrong Number")
    else:
        print("No, it is not an Armstrong Number")