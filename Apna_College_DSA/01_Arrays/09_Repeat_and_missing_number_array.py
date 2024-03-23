'''
You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4
'''

class Solution:
    def repeatedNumber(self, A):
        A = list(A)
        i = 0
        extra = -1

        while i < len(A):
            if (i+1) != A[i]:
                if A[i] == A[A[i] - 1]:
                    extra = A[i]
                    break
                    
                tmp = A[A[i] - 1]
                A[A[i] - 1] = A[i]
                A[i] = tmp

            else:
                i += 1

        total = ((len(A))*(len(A)+1))//2
        csum = sum(A)
        diff = abs(total-csum)

        if (total > csum):
            return [extra, extra + diff]
        return [extra, extra - diff]
    
solution = Solution()
print(solution.repeatedNumber([3, 1, 2, 5, 3]))