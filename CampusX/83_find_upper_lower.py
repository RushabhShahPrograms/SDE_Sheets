'''
Write a function that accepts a string and returns the number of upper case chars and lower case chars as a dictionary
'''

def count_case(s):
    upper = 0
    lower = 0

    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    
    return {"UPPERCASE":upper,"LOWERCASE":lower}

s = "Hello World"
print(count_case(s))