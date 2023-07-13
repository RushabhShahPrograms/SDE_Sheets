'''
In this post we will solve the problem “Check if given year is a leap year or not”.

Problem Statement: Check if the given year is a leap year or not.

Examples:

Example 1:
Input: 1996
Output: Yes
Explanation: Since 1996 is a leap year answer is “Yes”.

Example 2:
Input: 2000
Output: Yes

Explanation: Since 2000 is a leap year answer is “Yes”.
'''

year = int(input("Enter the year: "))
if(((year%4 == 0) and (year%100 != 0)) or (year%400 == 0)):
    print("Yes it is leap year")
else:
    print("No it is not leap year")