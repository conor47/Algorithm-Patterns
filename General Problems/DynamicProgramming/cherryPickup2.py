# You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

# You have two robots that can collect cherries for you:

#     Robot #1 is located at the top-left corner (0, 0), and
#     Robot #2 is located at the top-right corner (0, cols - 1).

# Return the maximum number of cherries collection using both robots by following the rules below:

#     From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
#     When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
#     When both robots stay in the same cell, only one takes the cherries.
#     Both robots cannot move outside of the grid at any moment.
#     Both robots should reach the bottom row in grid.

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        @lru_cache(None)
        def dp(row,col1,col2):
            if col1 < 0 or col1 >=n or col2 < 0 or col2 >= n:
                return float('-inf')
            res = 0
            res += grid[row][col1]
            if col1 != col2:
                res += grid[row][col2]
            if row != m-1:
                res += max(dp(row+1,new_col1,new_col2) for new_col1 in [col1,col1-1,col1+1] for new_col2 in [col2,col2-1,col2+1])
            return res
        return dp(0,0,n-1)

# Time complexity is O(M * N^2) due to memoization

# Space complexity is O(M * N^2) for memoization