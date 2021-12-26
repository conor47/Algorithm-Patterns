# In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

# Return the maximum amount of gold you can collect under the conditions:

#     Every time you are located in a cell you will collect all the gold in that cell.
#     From your position, you can walk one step to the left, right, up, or down.
#     You can't visit the same cell more than once.
#     Never visit a cell with 0 gold.
#     You can start and stop collecting gold from any position in the grid that has some gold.

 

# Example 1:

# Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
# Output: 24
# Explanation:
# [[0,6,0],
#  [5,8,7],
#  [0,9,0]]
# Path to get the maximum gold, 9 -> 8 -> 7.

# Example 2:

# Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# Output: 28
# Explanation:
# [[1,0,7],
#  [2,0,6],
#  [3,4,5],
#  [0,3,0],
#  [9,0,20]]
# Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

 

# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 15
#     0 <= grid[i][j] <= 100
#     There are at most 25 cells containing gold.

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n  = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def backtrack(row,col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
                return 0
            
            org = grid[row][col]
            grid[row][col] = 0
            ans = 0
            for x,y in directions:
                newRow = row + x
                newCol = col + y
                ans = max(ans,backtrack(newRow,newCol))
            grid[row][col] = org
            return ans + org
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans,backtrack(i,j))
        return ans

# Time complexity is O(3^k) where K <= 25. The first cell has up to 4 valid neighbours and the remaining cells have up to three valid neighrbours

# Space complexity is O(K)