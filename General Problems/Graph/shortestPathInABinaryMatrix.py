# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

#     All the visited cells of the path are 0.
#     All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

# The length of a clear path is the number of visited cells of this path.

# Input: grid = [[0,1],[1,0]]
# Output: 2

# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4

# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1

 

# Constraints:

#     n == grid.length
#     n == grid[i].length
#     1 <= n <= 100
#     grid[i][j] is 0 or 1

import collections

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        if grid[rows-1][cols-1] != 0 or grid[0][0] != 0:
            return -1
        target = (rows-1,cols-1)
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        queue = collections.deque()
        grid[0][0] = 1
        queue.append((0,0))
        
        while len(queue):
            row,col = queue.popleft()
            distance = grid[row][col]
            if (row,col) == target:
                return distance
            for x,y in directions:
                new_row = row+x
                new_col = col+y
                if self.isValid(new_row,new_col,grid):
                    queue.append((new_row,new_col))
                    grid[new_row][new_col] = distance + 1
        return -1
            
            
            
            
    def isValid(self,row,col,grid):
        rowLimit, colLimit = len(grid),len(grid[0])
        if row < 0 or row >= rowLimit or col < 0 or col >= colLimit or grid[row][col] != 0:
            return False
        return True

# Time complexity is O(N). Each cell is guaranteed to be visited only once. Identifying the unvisted neighbours for each cell is a constant
# time operation

# Space complexity is O(N)

# Space complexity is 