# Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid) 
        visited = set()
        q = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                     q.append((i,j,0))        
                     visited.add((i,j))
        if len(q) == 0 or len(q) == n**2:
            return -1
        maxDist = 0
        while q:
            row,col,dist = q.pop(0)
            maxDist = max(maxDist,dist)
            
            for newRow, newCol in self.generate(row,col,n, grid):
                if (newRow, newCol) not in visited:
                    visited.add((newRow,newCol))
                    q.append((newRow, newCol, dist+1))
        return maxDist         
        
        
    def generate(self,row,col,n, grid):
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for direction in directions:
            newRow = row + direction[0]
            newCol = col + direction[1]
            if newRow < 0 or newRow >= n or newCol < 0 or newCol >= n or grid[newRow][newCol] == 1 :
                continue
                
            else:
                yield(newRow, newCol)

# Time complexity is O(N) is the number of cells in the grid

# Space complexity is O(N)