# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

#     Any live cell with fewer than two live neighbors dies as if caused by under-population.
#     Any live cell with two or three live neighbors lives on to the next generation.
#     Any live cell with more than three live neighbors dies, as if by over-population.
#     Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        
        newBoard = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                live = 0
                current = board[i][j]
                new = 0
                for new_row,new_col in self.findNeighbours(i,j,rows,cols):
                    if board[new_row][new_col] == 1:
                        live += 1
                if current:
                    if live < 2:
                        new = 0  
                    elif live <=3:
                        new = 1
                    elif live >3:
                        new = 0
                else:
                    if live == 3:
                        new = 1
                newBoard[i][j] = new
        for i in range(rows):
            for j in range(cols):
                board[i][j] = newBoard[i][j]
                        
    def findNeighbours(self,row,col,rows,cols):
        directions = [(-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,-1),(1,0),(1,1)]
        for x,y in directions:
            new_row = row + x
            new_col = col + y
            if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                continue
            yield(new_row,new_col)

# Time complexity is O(N*M)

# Space complexity is O(N*M)