# There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

# Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return the shortest distance for the ball to stop at the destination. If the ball cannot stop at destination, return -1.

# The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).

# You may assume that the borders of the maze are all walls (see examples).

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        q = [(start[0],start[1],0)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        n = len(maze)
        m = len(maze[0])
        if not m or not n or start == destination:
            return 0
        visited = {(start[0],start[1]):0}
        
        while q:
            i,j,steps = q.pop(0)
            
            for dx,dy in directions:
                
                x,y,d = i,j,steps
                
                
                while 0<= x+dx < n and 0 <= y+dy < m and maze[x + dx][y + dy] == 0:
                    x += dx 
                    y += dy
                    d += 1
                
                if (x,y) not in visited or ((x,y) in visited and visited[(x,y)] > d):
                    visited[(x,y)] = d
                
                    if (x,y) != (destination[0],destination[1]):
                        q.append((x,y,d))
        return visited.get((destination[0],destination[1]),-1)

# Time complexity is O(M*N * max(M,N))

# Space complexity is O(M * N)