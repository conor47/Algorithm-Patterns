# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

class Solution:
    
    def __init__ (self):
        self.root = TrieNode()
    
    def insert(self,word):
        cur = self.root
        for char in word:
            cur = cur.children[char]
        cur.isWord = word
        
            
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.insert(word)
            
        res = []
        rowNum = len(board) 
        colNum = len(board[0])
        
        def backtracking(row,col,parent):
            letter = board[row][col]
            cur = parent.children.get(letter)

            if cur.isWord:
                word = cur.isWord
                cur.isWord = False
                res.append(word)
            board[row][col] = '#' 
            
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in cur.children:
                    continue
                backtracking(newRow,newCol,cur)
            board[row][col] = letter
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in self.root.children:
                    backtracking(i,j,self.root)
        return res
                
class TrieNode:
    
    def __init__ (self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

# Time complexity is O(M(4 * 3 ^ L-1)). L is the length of the longest word. Starting from some cell we initially have 4 directions to explore.
# Assuming each direction is valid then during the following exploration we will have at most 3 directios to explore.

# Space complexity is O(N) where N is the total number of letters in the words