'''
Find the length of a given string without using the len() function.
'''

def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

# Test the function
s = input("Enter a string: ")
print(f"The length of the string is {string_length(s)}")
