# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        def perimeterCount(row,col):
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            count = 0 
            
            for x,y in directions:
                newRow = row+x 
                newCol = col+y
                
                if newRow < 0 or newRow >= rows or newCol < 0 or newCol >= cols:
                    count += 1
                
                elif grid[newRow][newCol] == 0:
                    count += 1
            
            return count
        
        res = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res += perimeterCount(i,j)
        
        return res

# Time complexity is O(N) where N is the number of cells in the grid

# Space complexity is O(1)