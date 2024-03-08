'''
Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.
'''

sum = 0
count = 0

while True:
    num = float(input("Enter a number  (or 0 to stop): "))
    if num==0:
        break
    sum+= num
    count += 1

if count>0:
    average = sum/count
    print(f"The sum of the numbers is {sum} and the average is {average}")
else:
    print("No numbers were entered.")