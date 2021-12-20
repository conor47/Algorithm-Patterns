# ou are given an m x n integer matrix grid, and three integers row, col, and color. Each value in the grid represents the color of the grid square at that location.

# Two squares belong to the same connected component if they have the same color and are next to each other in any of the 4 directions.

# The border of a connected component is all the squares in the connected component that are either 4-directionally adjacent to a square not in the component, or on the boundary of the grid (the first or last row or column).

# You should color the border of the connected component that contains the square grid[row][col] with color.

# Return the final grid.

 

# Example 1:

# Input: grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
# Output: [[3,3],[3,2]]

# Example 2:

# Input: grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
# Output: [[1,3,3],[2,3,3]]

# Example 3:

# Input: grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
# Output: [[2,2,2],[2,1,2],[2,2,2]]

 

# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 50
#     1 <= grid[i][j], color <= 1000
#     0 <= row < m
#     0 <= col < n

# First over engineered solution

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        visited = set()    
        q = [(row,col)]
        currentColor = grid[row][col]
        boundary = set()
        while q:
            row,col = q.pop(0)
            visited.add((row,col))
            if self.isBorder(row,col,grid,currentColor):
                boundary.add((row,col))
            for newRow,newCol in self.nextMove(row,col,grid,currentColor):
                if (newRow, newCol) not in visited:
                    q.append((newRow,newCol))
                    visited.add((newRow,newCol))
        for row,col in boundary:
            grid[row][col] = color
        return grid         
    
    def nextMove(self, row, col, grid, currentColor):
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for pair in directions:
            newRow = row + pair[0]
            newCol = col + pair[1] 
            
            if newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid[0]) or grid[newRow][newCol] != currentColor:
                continue
            
            else:
                yield (newRow,newCol)
    
    def isBorder(self,row,col,grid,currentColor):
        if row == 0 or col == 0 or row == len(grid)-1 or col == len(grid[0])-1:
            return True
        
        elif grid[row-1][col] != currentColor or grid[row+1][col] != currentColor or grid[row][col-1] != currentColor or grid[row][col+1] != currentColor:
            return True
        
        else:
            return False

# Time complexity is O(N) where N is the number of cells in the grid

# Space complexity is O(N)

# Simpler DFS solution

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        self.dfs(row,col,grid,grid[row][col])    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    grid[i][j] = color
        return grid 
    
    def dfs(self,row,col,grid,color):
        if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != color):
            return
        grid[row][col] = -color
        self.dfs(row - 1,col,grid,color)
        self.dfs(row+1,col,grid,color)
        self.dfs(row,col-1,grid,color)
        self.dfs(row,col+1,grid,color)
        if( row >  0 and row < len(grid)-1 and col > 0 and col < len(grid[0])-1 and color == abs(grid[row+1][col]) and color == abs(grid[row-1][col]) and color == abs(grid[row][col-1]) and color == abs(grid[row][col+1])):
            grid[row][col] = color