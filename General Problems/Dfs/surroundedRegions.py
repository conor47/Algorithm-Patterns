# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

# Example 2:

# Input: board = [["X"]]
# Output: [["X"]]

 

# Constraints:

#     m == board.length
#     n == board[i].length
#     1 <= m, n <= 200
#     board[i][j] is 'X' or 'O'.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        
        for i in range(rows):
            if board[i][0] == 'O':
                self.dfs(board,i,0)
            if board[i][cols - 1]:
                self.dfs(board,i,cols - 1)
        
        for i in range(cols):
            if board[0][i] == 'O':
                self.dfs(board,0,i)
            if board[rows-1][i]:
                self.dfs(board,rows-1,i)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '*':
                    board[i][j] = 'O'
         
    def dfs(self, board,row,col):
        if(row < 0 or row >=len(board) or col < 0 or col >= len(board[0]) or board[row][col] != 'O'):
            return
        
        board[row][col] = '*'
        
        self.dfs(board,row+1,col)
        self.dfs(board,row-1,col)
        self.dfs(board,row,col+1)
        self.dfs(board,row,col-1)

# Time complexity is (M * N) where M and N are the dimensions of the grid

# Space complexity is O (M * N) 