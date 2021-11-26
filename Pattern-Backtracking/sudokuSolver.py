# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

#     Each of the digits 1-9 must occur exactly once in each row.
#     Each of the digits 1-9 must occur exactly once in each column.
#     Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

# The '.' character indicates empty cells.

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row,col = self.nextPosition(board)
        if row is None:
            return True
        
        for guess in range(1,10):
            if self.validate(board,row,col,str(guess)):
                board[row][col] = str(guess)
                if self.solveSudoku(board):
                    return True
            
            board[row][col] = '.'
        return False
    
    def nextPosition(self,board):
        for row in range (9):
            for col in range(9):
                if board[row][col] == '.':
                    return row,col
        return None,None
    
    def validate(self,board,i,j,guess):
    
        row = board[i]
        
        if guess in row:
            return False
        
        col = [board[i][j] for i in range(9)]
        
        if guess in col:
            return False
        
        rowStart = i // 3 * 3
        colStart = j // 3 * 3 
         
        for x in range(rowStart,rowStart+3):
            for y in range(colStart,colStart+3):
                if board[x][y] == guess:
                    return False
        return True