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
