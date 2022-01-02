# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        rows,cols = len(matrix), len(matrix[0])
            
        def dfs(row,col,prev):
            if row < 0 or col < 0 or row >= rows or col >= cols or matrix[row][col] <= prev:
                return 0
            if (row,col) in dp:
                return dp[(row,col)]
            res = 1
            res = max(res,1 + dfs(row+1,col,matrix[row][col]))
            res = max(res,1 + dfs(row-1,col,matrix[row][col]))
            res = max(res,1 + dfs(row,col+1,matrix[row][col]))
            res = max(res,1 + dfs(row,col-1,matrix[row][col]))
            dp[(row,col)] = res
            return res
        
        for row in range(rows):
            for col in range(cols):
                dfs(row,col,-1)
        return max(dp.values())

# Time complexity is O(N * M)

# Space complexity is O(M * N) for the memoization dictionary