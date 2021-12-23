# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

# You may change 0's to 1's to connect the two islands to form one island.

# Return the smallest number of 0's you must flip to connect the two islands.

 

# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 1

# Example 2:

# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2

# Example 3:

# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1

 

# Constraints:

#     n == grid.length == grid[i].length
#     2 <= n <= 100
#     grid[i][j] is either 0 or 1.
#     There are exactly two islands in grid.

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        def dfs(i,j):
            queue.append((i,j))
            grid[i][j] = -1
            
            for x, y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if x < 0 or x >= n or y < 0 or y >=m or grid[x][y] !=1:
                    continue
                else:
                    dfs(x,y)
        def find():
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1:
                        return i,j
        queue = []
        dfs(*find())
       
    
        steps = 0
        while queue:
            new = []
            for row,col in queue:
                for x,y in ((row+1,col),(row-1,col),(row,col+1),(row,col-1)):
                    if 0 <= x < n and 0 <= y < m:
                        if grid[x][y] == 1:
                            return steps
                        elif not grid[x][y]:
                            grid[x][y] = -1
                            new.append((x,y))
            steps += 1
            queue = new

# Time complexity is O(N) where N is the number of cells in the grid

# Space complexity is O(N)