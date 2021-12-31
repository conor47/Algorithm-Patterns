# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        @lru_cache(None)
        def recurse(row,col,moves):
            if moves > maxMove:
                return 0
            if row < 0 or col < 0 or row >= m or col >= n:
                return 1
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            res = 0
            for x,y in directions:
                res += recurse(row+x,col+y,moves+1)    
            return res
        return recurse(startRow,startColumn,0) % (pow(10,9) + 7)
