# You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

# You are given an m x n character matrix, grid, of these different types of cells:

#     '*' is your location. There is exactly one '*' cell.
#     '#' is a food cell. There may be multiple food cells.
#     'O' is free space, and you can travel through these cells.
#     'X' is an obstacle, and you cannot travel through these cells.

# You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

# Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        seen = set()
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        
        def findStart():
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == '*':
                        return(i,j) 
                    
        x,y = findStart()
        queue.append((x,y,0))
        seen.add((x,y))
        while queue:
            row,col,dist = queue.popleft()
            if grid[row][col] == '#':
                return dist
            
            for x,y in directions:
                new_row = row + x
                new_col = col + y
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or (new_row,new_col) in seen or grid[new_row][new_col] == 'X':
                    continue
                queue.append((new_row,new_col,dist+1))
                seen.add((new_row,new_col))
        return -1

# Time complexity is O(N * M) as in the worst case we must visit every cell in the grid

# Space complexity is O(N * M) for the seen set