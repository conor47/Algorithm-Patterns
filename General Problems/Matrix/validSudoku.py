# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:

#     A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#     Only the filled cells need to be validated according to the mentioned rules.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if self.validate(board,i,j):
                        continue
                    else:
                        return False
        return True

    def validate(self,board,i,j):
        val = board[i][j]
        row = board[i]
        
        for x in range (9):
            if row[x] == val and x != j:
                return False
        
        col = [board[i][j] for i in range(9)]
        
        for x in range (9):
            if col[x] == val and  x != i:
                return False
        
        rowStart = i // 3 * 3
        colStart = j // 3 * 3 
         
        for x in range(rowStart,rowStart+3):
            for y in range(colStart,colStart+3):
                if board[x][y] == val and x != i and y != j:
                    return False
        return True

