'''
Problem Statement: Check if the number is a Harshad(or Niven) number or not.

Examples:

Example 1:
Input: 378
Output: Yes it is a Harshad number.
Explanation: 3+7+8=18. 378 is divisible by 18. Therefore 378 is a harshad number.

Example 2:
Input: 379
Output: No
 it is not a Harshad number.
Explanation: 3+7+9=19. 379 is not divisible by 19. Therefore 379 is a harshad number.
'''

n = int(input("Enter the value: "))
temp = n
sum = 0
while(temp!=0):
    sum += temp%10
    temp //=10

if(n%sum==0):
    print("Yes it is Harshad Number")
else:
    print("No it is not Harshad Number")