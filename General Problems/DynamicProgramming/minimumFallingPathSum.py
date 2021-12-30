# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix) 
        
        @lru_cache(maxsize = None)
        def recursive(row,col):
            if row < 0 or row >= n or col < 0 or col >= n:
                return float('inf')
            
            path = matrix[row][col]
            if row < n-1:
                path += min(recursive(row+1,col),recursive(row+1,col-1),recursive(row+1,col+1))
            return path
        
        m = float('inf')
        for i in range(n):
            m = min(m,recursive(0,i))
        return m

# Bottom up solution

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n ==1:
            return min(matrix[0])
        dp = [[0 for i in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[0][i] = matrix[0][i]
        
        for i in range(1,n):
            for j in range(n):
                if j  == 0:
                    dp[i][j] = matrix[i][j]+ min(dp[i-1][j], dp[i-1][j+1])
                elif j == n-1:
                    dp[i][j] =matrix[i][j] + min(dp[i-1][j], dp[i-1][j-1])
                else:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i-1][j+1], dp[i-1][j-1])
        return min(dp[n-1])