'''
Given two strings A and B, the task is to convert A to B if possible. The only operation allowed is to put any character from A and insert it at front. Find if it’s possible to convert the string. If yes, then output minimum no. of operations required for transformation.

Examples: 

Input:  A = "ABD", B = "BAD"
Output: 1
Explanation: Pick B and insert it at front.
Input:  A = "EACBD", B = "EABCD"
Output: 3
Explanation: Pick B and insert at front, EACBD => BEACD
             Pick A and insert at front, BEACD => ABECD
             Pick E and insert at front, ABECD => EABCD
'''

def minOps(A, B):
	m = len(A)
	n = len(B)

	# This part checks whether conversion is possible or not
	if n != m:
		return -1

	count = [0] * 256

	for i in range(n):	 # count characters in A
		count[ord(B[i])] += 1
	for i in range(n):	 # subtract count for every char in B
		count[ord(A[i])] -= 1
	for i in range(256): # Check if all counts become 0
		if count[i]:
			return -1

	# This part calculates the number of operations required
	res = 0
	i = n-1
	j = n-1
	while i >= 0:
	
		# if there is a mismatch, then keep incrementing
		# result 'res' until B[j] is not found in A[0..i]
		while i>= 0 and A[i] != B[j]:
			i -= 1
			res += 1

		# if A[i] and B[j] match
		if i >= 0:
			i -= 1
			j -= 1

	return res

# Driver program
A = "EACBD"
B = "EABCD"
print ("Minimum number of operations required is " + str(minOps(A,B)))