'''
Pattern searching is an important problem in computer science. When we do search for a string in a notepad/word file, browser, or database, pattern searching algorithms are used to show the search results.

A typical problem statement would be- 

” Given a text txt[0..n-1] and a pattern pat[0..m-1] where n is the length of the text and m is the length of the pattern, write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m. “
Examples: 

Input: txt[] = “THIS IS A TEST TEXT”

pat[] = “TEST”

Output: Pattern found at index 10

Input: txt[] = “AABAACAADAABAABA”

pat[] = “AABA”

Output: Pattern found at index 0

Pattern found at index 9

Pattern found at index 12
'''

# Python3 Program for Bad Character Heuristic
# of Boyer Moore String Matching Algorithm

NO_OF_CHARS = 256


def badCharHeuristic(string, size):

	badChar = [-1]*NO_OF_CHARS

	for i in range(size):
		badChar[ord(string[i])] = i

	return badChar


def search(txt, pat):

	m = len(pat)
	n = len(txt)

	badChar = badCharHeuristic(pat, m)

	s = 0
	while(s <= n-m):
		j = m-1

		while j >= 0 and pat[j] == txt[s+j]:
			j -= 1

		if j < 0:
			print("Pattern occur at shift = {}".format(s))
			
			s += (m-badChar[ord(txt[s+m])] if s+m < n else 1)
		else:
			s += max(1, j-badChar[ord(txt[s+j])])


# Driver program to test above function
def main():
	txt = "ABAAABCD"
	pat = "ABC"
	search(txt, pat)


if __name__ == '__main__':
	main()