# You are given an m x n grid where each cell can have one of three values:

#     0 representing an empty cell,
#     1 representing a fresh orange, or
#     2 representing a rotten orange.

# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

 

# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 10
#     grid[i][j] is 0, 1, or 2.

import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxTime = 0
        fresh_oranges = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        def getNeighbours(row,col):
            for x,y in directions:
                new_row = row+x
                new_col = col+y
            
                if new_row < 0 or new_row >=rows or new_col < 0 or new_col >= cols:
                    continue
                if grid[new_row][new_col] != 1:
                    continue
                yield(new_row,new_col)
        
        queue = collections.deque()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        
        while len(queue):
            row,col,time = queue.popleft()
            maxTime = max(maxTime,time)
            
            for neighbor_row,neighbor_col in getNeighbours(row,col):
                grid[neighbor_row][neighbor_col] = 2
                fresh_oranges -= 1
                queue.append((neighbor_row,neighbor_col,time+1))
        
        return maxTime if fresh_oranges == 0 else -1

# Time complexity is O(N) where N is the size of the grid. The initial scan and performing the BFS take O(N) time each

# Space complexity is O(N) as in the worst case if every cell is a rotting orange our queue will store N items.
