# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxLen = 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1],dp[i-1][j-1]) + 1   
                    maxLen = max(maxLen, dp[i][j])
               
        return maxLen ** 2
        
# Time complexity is O(N*M)
# Space complexity is (N*M)