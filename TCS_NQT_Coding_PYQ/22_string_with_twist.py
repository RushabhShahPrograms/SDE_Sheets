'''
The program will recieve 3 English words inputs from STDIN

These three words will be read one at a time, in three separate line
The first word should be changed like all vowels should be replaced by %
The second word should be changed like all consonants should be replaced by #
The third word should be changed like all char should be converted to upper case
Then concatenate the three words and print them
Other than these concatenated word, no other characters/string should or message should be written to STDOUT

For example if you print how are you then output should be h%wa#eYOU.

You can assume that input of each word will not exceed more than 5 chars 
'''

a = input()
b = input()
c = input()

x = len(a)
y = len(b)

for i in range(x):
    if a[i] in ['a', 'e', 'i', 'o', 'u']:
        a = a[:i] + '%' + a[i+1:]

for j in range(y):
    if b[j].isalpha():
        b = b[:j] + '#' + b[j+1:]

for j in range(y):
    if b[j].isupper():
        b = b[:j] + '#' + b[j+1:]

c = c.upper()

print(a+b+c)
