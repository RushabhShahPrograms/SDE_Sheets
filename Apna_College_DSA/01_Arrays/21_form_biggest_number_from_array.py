'''
Given an array of strings arr[] of length n representing non-negative integers, arrange them in a manner, such that, after concatanating them in order, it results in the largest possible number. Since the result may be very large, return it as a string.

Example 1:

Input: 
n = 5
arr[] =  {"3", "30", "34", "5", "9"}
Output: "9534330"
Explanation: 
Given numbers are  {"3", "30", "34", "5", "9"}, 
the arrangement "9534330" gives the largest value.
Example 2:

Input: 
n = 4
arr[] =  {"54", "546", "548", "60"}
Output: "6054854654"
Explanation: 
Given numbers are {"54", "546", "548", "60"}, the 
arrangement "6054854654" gives the largest value.
'''

from functools import cmp_to_key

def compare(a,b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return ((int(ba)>int(ab))-(int(ba)<int(ab)))

def arrange(arr):
    arr = sorted(arr,key=cmp_to_key(compare))
    return ''.join([str(i) for i in arr])

print(arrange(["3","30","34","5","9"]))
print(arrange(["54","546","548","60"]))