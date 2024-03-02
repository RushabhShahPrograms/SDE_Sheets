'''
User will input (3ages).Find the oldest one.
'''
age1 = int(input("Enter the age of first:"))
age2 = int(input("Enter the age of second:"))
age3 = int(input("Enter the age of third:"))

if(age1 > age2 and age1 > age3):
    print("Age1 is oldest")
elif(age2 > age1 and age2 > age3):
    print("Age2 is oldest")
else:
    print("Age3 is oldest")