# There is an m x n grid, where (0, 0) is the top-left cell and (m - 1, n - 1) is the bottom-right cell. You are given an integer array startPos where startPos = [startrow, startcol] indicates that initially, a robot is at the cell (startrow, startcol). You are also given an integer array homePos where homePos = [homerow, homecol] indicates that its home is at the cell (homerow, homecol).

# The robot needs to go to its home. It can move one cell in four directions: left, right, up, or down, and it can not move outside the boundary. Every move incurs some cost. You are further given two 0-indexed integer arrays: rowCosts of length m and colCosts of length n.

#     If the robot moves up or down into a cell whose row is r, then this move costs rowCosts[r].
#     If the robot moves left or right into a cell whose column is c, then this move costs colCosts[c].

# Return the minimum total cost for this robot to return home.

# Could be more efficiently implemented by doing some basic row / column math but this
# is just a straighforward method

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        total = 0
        
        row,col = startPos[0], startPos[1]
        if row < homePos[0]:
            while row<homePos[0]:
                row += 1
                total += rowCosts[row]
        elif row > homePos[0]:
            while row > homePos[0]:
                row -= 1
                total += rowCosts[row]
       
        if col > homePos[1]:
            while col > homePos[1]:
                col -= 1
                total += colCosts[col]
        elif col < homePos[1]:
            while col < homePos[1]:
                col += 1
                total += colCosts[col]
        return total

# Time complexity is O(N + M) as in the worst case we need to traverse the grid from corner to corner 

# Space complexity is O(1)