'''
Count the frequency of a particular character in a provided string. Eg 'hello how are you' is the string, the frequency of h in this string is 2.
'''

def count_char(s,char):
    return s.count(char)

s = input("Enter a string: ")
char = input("Enter a character: ")
print(f"The frequency of '{char}' in the string is {count_char(s,char)}")