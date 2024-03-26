'''
Given a string S, the task is to print all the duplicate characters with their occurrences in the given string.

Example:

Input: S = “geeksforgeeks”
Output:

e, count = 4
g, count = 2
k, count = 2
s, count = 2

Explanation: e,g,k,and s are characters which are occured in string in more than one times.
'''

def printDups(Str):

	count = {}
	for i in range(len(Str)):
		if(Str[i] in count):
			count[Str[i]] += 1
		else:
			count[Str[i]] = 1
		#increase the count of characters by 1 

	for it,it2 in count.items(): #iterating through the unordered map 
		if (it2 > 1): #if the count of characters is greater than 1 then duplicate found
			print(str(it) + ", count = "+str(it2))
	
# Driver code
Str = "abcdababab cdcdcaababbaabb"
printDups(Str)