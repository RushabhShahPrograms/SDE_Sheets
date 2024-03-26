'''
Given two strings S and P. Find the smallest window in the string S consisting of all the characters(including duplicates) of the string P.  Return "-1" in case there is no such window present. In case there are multiple such windows of same length, return the one with the least starting index.
Note : All characters are in Lowercase alphabets. 

Example 1:

Input:
S = "timetopractice"
P = "toc"
Output: 
toprac
Explanation: "toprac" is the smallest
substring in which "toc" can be found.
Example 2:

Input:
S = "zoomlazapzo"
P = "oza"
Output: 
apzo
Explanation: "apzo" is the smallest 
substring in which "oza" can be found.
Your Task:
You don't need to read input or print anything. Your task is to complete the function smallestWindow() which takes two string S and P as input paramters and returns the smallest window in string S having all the characters of the string P. In case there are multiple such windows of same length, return the one with the least starting index. 

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(n) n = len(p)

 

Constraints: 
1 ≤ |S|, |P| ≤ 10^5
'''

def smallestWindow(S,P):
    from collections import Counter
    len1 = len(S)
    len2 = len(P)

    hash_pat = Counter(P)
    hash_str = Counter()

    start, start_index, min_len = 0,-1,float('inf')

    count = 0
    for j in range(len1):
        hash_str[S[j]] += 1
        if hash_str[S[j]] <= hash_pat[S[j]]:
            count += 1
        if count == len2:
            while hash_str[S[start]] > hash_pat[S[start]]:
                hash_str[S[start]] -= 1
                start += 1
            
            len_window = j - start + 1
            if min_len > len_window:
                min_len = len_window
                start_index = start
    
    if start_index == -1:
        return "-1"
    else:
        return S[start_index : start_index + min_len]
    

print(smallestWindow("timetopractice", "toc"))  # Output: "toprac"
print(smallestWindow("zoomlazapzo", "oza"))  # Output: "apzo"