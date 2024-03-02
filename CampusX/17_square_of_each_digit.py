'''
Write a program that will take three digits from the user and add the square of each digit.
'''

def sum_of_squares(num):
    return sum(map(lambda x:int(x)**2, str(num)))

user = int(input("Enter a three digit number: "))
if 100 <= user <=999:
    result = sum_of_squares(user)
    print("The sum of squares is: ",result)
else:
    print("Please enter a valid three-digit number")