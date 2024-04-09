'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
'''

def exist(board,word):
    def backtrack(i,j,k):
        if board[i][j] != word[k]:
            return False
        
        if k == len(word) - 1:
            return True
        
        temp = board[i][j]
        board[i][j] = '#'
        
        for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                if backtrack(x,y,k+1):
                    return True
        
        board[i][j] = temp
        return False
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtrack(i,j,0):
                return True
    
    return False

board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"
print(exist(board1,word1))

board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word2 = "SEE"
print(exist(board2, word2))

board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word3 = "ABCB"
print(exist(board3, word3))