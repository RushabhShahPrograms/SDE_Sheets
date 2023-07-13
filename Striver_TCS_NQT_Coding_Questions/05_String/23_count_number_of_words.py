'''
Problem statement − We are given a string we need to count the number of words in the string
'''

test_string = "Tutorials point is a learning platform"
#original string
print ("The original string is : " + test_string)
# using split() function
res = len(test_string.split())
# total no of words
print ("The number of words in string are : " + str(res))