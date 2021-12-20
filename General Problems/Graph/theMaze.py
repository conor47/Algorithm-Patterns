# There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

# Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

# You may assume that the borders of the maze are all walls (see examples).

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        q = [start]
        n = len(maze)
        m = len(maze[0])
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        
        while q:
            i,j = q.pop(0)
            maze[i][j] = 2
            
            if i == destination[0] and j == destination[1]:
                return True
            
            for a,b in directions:
                row = i + a
                col = j + b
                
                while 0<= row < n and 0 <= col < m and maze[row][col] != 1:
                    row += a
                    col += b
                row -= a
                col -= b
                
                if maze[row][col] == 0:
                    q.append((row,col))
        return False
                
# Time complexity is O(N) where N is the number of cells in the maze

# Space complexity is O(N)