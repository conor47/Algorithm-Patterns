# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

class Solution:
    res = 0
    def totalNQueens(self, n: int) -> int:
        if n == 0:
            return 0
        self.nQueens(n,0,[])
        return self.res
        
                
    def nQueens(self,n,row,placements):
        if row == n:
            self.res += 1
            return 
        
        else:
            for j in range(n):
                placements.append(j)
                if self.isValid(placements):
                    self.nQueens(n,row+1,placements)
                placements.pop()
        
                
    def isValid(self,placements):
        rowId = len(placements) - 1
        
        for i in range(rowId):
            diff = abs(placements[i] - placements[rowId])
            if diff == 0 or diff == rowId - i:
                return False
        return True

# Time complexity is O(N!)

# Space complexity is O(N)
