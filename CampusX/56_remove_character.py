'''
Write a program which can remove a articular character from a string.
'''

def remove_char(string,char):
    return string.replace(char,'')

print(remove_char("Hello World!","W"))