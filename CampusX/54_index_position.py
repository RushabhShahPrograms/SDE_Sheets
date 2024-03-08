'''
Find the index position of a particular character in another string
'''

def find_index(string,char):
    try:
        return string.index(char)
    except ValueError:
        return "Character not found in string"
    
print(find_index("Hello, World!","W"))