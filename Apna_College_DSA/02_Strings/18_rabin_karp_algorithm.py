'''
Given a text T[0. . .n-1] and a pattern P[0. . .m-1], write a function search(char P[], char T[]) that prints all occurrences of P[] present in T[] using Rabin Karp algorithm. You may assume that n > m.

Examples: 

Input:  T[] = “THIS IS A TEST TEXT”, P[] = “TEST”
Output: Pattern found at index 10

Input:  T[] =  “AABAACAADAABAABA”, P[] =  “AABA”
Output: Pattern found at index 0
              Pattern found at index 9
              Pattern found at index 12
'''

# Function to search for pattern P[] in text T[] using Rabin-Karp algorithm
def search(P, T):
    # Define prime number for hashing
    prime = 101
    
    # Length of pattern and text
    m = len(P)
    n = len(T)
    
    # Calculate hash value for pattern and the first window of text
    hash_P = 0
    hash_T = 0
    for i in range(m):
        hash_P = (hash_P + ord(P[i])) % prime
        hash_T = (hash_T + ord(T[i])) % prime
    
    # Iterate through the text with a sliding window approach
    for i in range(n - m + 1):
        # Check if the hash values match, if they do, perform a character by character comparison
        if hash_P == hash_T:
            match = True
            for j in range(m):
                if P[j] != T[i + j]:
                    match = False
                    break
            if match:
                print("Pattern found at index", i)
        
        # Calculate hash value for the next window of text
        if i < n - m:
            hash_T = (hash_T - ord(T[i]) + ord(T[i + m])) % prime
            # Make sure the hash value is positive
            if hash_T < 0:
                hash_T += prime

# Test cases
T1 = "THIS IS A TEST TEXT"
P1 = "TEST"
print("Test Case 1:")
search(P1, T1)

T2 = "AABAACAADAABAABA"
P2 = "AABA"
print("\nTest Case 2:")
search(P2, T2)