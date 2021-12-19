# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        land = 0 
        boundary = set()
        
        def nextMove(row, col):
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]) or grid[new_row][new_col] == 0 or (new_row, new_col) in visited:
                    continue
                else:
                    yield (new_row,new_col)
        
        
        
        for i in range (row):
            for j in range (col):
                if grid[i][j] == 1:
                    land += 1 
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        boundary.add((i,j))
        
        q = []
        visited = set()
        for row,col in boundary:
            q.append((row,col))
            visited.add((row,col))
        count = 0 
        while q:
            row,col = q.pop(0) 
            visited.add((row,col))
            count += 1
            for new_row, new_col in nextMove(row,col):
                    q.append((new_row, new_col))
                    visited.add((new_row,new_col))
        return land - count

# Time complexity is O(N * M)

# Space complexity is O(N * M)

# Alternative approach is to flood fill land from the boundary and then count the remaining land

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        boundary = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        boundary.add((i,j))
        
        def nextMove(row, col):
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]) or grid[new_row][new_col] == 0:
                    continue
                else:
                    yield (new_row,new_col)
        
        def floodFill(row,col):
            grid[row][col] = 0
            for new_row,new_col in nextMove(row,col):
                floodFill(new_row,new_col)
        
        
        
        for row,col in boundary:
            floodFill(row,col)
        land = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    land += 1
        return land
        