'''
Assume a list with numbers from 1 to 10 and then convert it into a dictionary where the  key would be the numbers of the list and the values would be the square of those numbers
'''

numbers = list(range(1, 11))

squares = {number: number**2 for number in numbers}

print(squares)
