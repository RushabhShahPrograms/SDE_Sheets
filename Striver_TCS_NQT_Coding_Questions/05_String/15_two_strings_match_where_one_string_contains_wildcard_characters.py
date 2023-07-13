'''
Two String match where one contains wildcard character
In this page we will learn about how to check if two strings match where one string contains wildcard characters.(Two string match where One String Contain Wild card character)

Make a function solve() with boolean as a return type, that will return true if the strings match else it will return false. Then we will check whether function returns True or false and prints the respective message to output.

Algorithm:
-> Initialize the variables.
-> Accept the input.
-> Check both the strings character by character.
-> If a character of wild  string contains a ‘*’, take the next character from wild string and check for that character in string which you want to match.
    -> If they match, continue checking the next character
    -> Else return false.
-> If the character of wild string contains a ‘?’, check if the immediate next character of wild string and the next character of string to be matched.
    -> If they match, continue checking  the next characters.
    -> Else, return false.
-> Print result.
'''

def match(first, second):
    if len(first) == 0 and len(second) == 0:
        return True

    if len(second) > 1 and second[0] == '*' and len(first) == 0:
        return False

    if (len(second) > 1 and second[0] == '*'):
        return match(first[1:], second) or match(first, second[1:])

    if len(first) > 0 and len(second) > 0 and (first[0] == second[0]):
        return match(first[1:], second[1:])

    return False

str1 = "abc"
str2 = "a*c"
if match(str1, str2):
    print("True")
else:
    print("False")