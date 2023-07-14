'''
Explanation:
To check whether a year is leap or not
Step 1:

We first divide the year by 4.
If it is not divisible by 4 then it is not a leap year.
If it is divisible by 4 leaving remainder 0 
Step 2:

We divide the year by 100
If it is not divisible by 100 then it is a leap year.
If it is divisible by 100 leaving remainder 0
Step 3:

We divide the year by 400
If it is not divisible by 400 then it is a leap year.
If it is divisible by 400 leaving remainder 0 
'''

num = int(input("Enter the year you want to check if is leap year or not: "))
if(num%4 == 0):
    if(num%100 == 0):
        if(num%400 == 0):
            print("The year {} is a leap year".format(num))
        else:
            print("The year {} is Not a leap year".format(num))
    else:
        print("The year {} is a leap year".format(num))
else:
    print("The year {} is Not a leap year".format(num))