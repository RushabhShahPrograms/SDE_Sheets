'''
Count the number of vowels in a string provided by the user
'''

def count_vowels(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)

print(count_vowels("Hello, World!"))