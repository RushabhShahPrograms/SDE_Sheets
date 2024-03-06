'''
Find the reverse of a number provided by the user(any number of digit)
'''

num = int(input("Enter a number: "))

reverse_num = 0
while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num //= 10

print(f"The reverse of the number is {reverse_num}")