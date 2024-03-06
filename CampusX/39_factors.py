'''
Take a number from the user and find the number of digits in it
'''


num = int(input("Enter a number: "))
print(f"The factors of {num} are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)