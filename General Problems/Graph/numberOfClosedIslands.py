# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

# Return the number of closed islands.

# Flood fill land touching the boundary. Then count and flood fill remaining land

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        def nextMove(row,col):
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            
            for direction in directions:
                newRow = row + direction[0]
                newCol = col + direction[1]
                
                if newRow < 0 or newRow >= rows or newCol < 0 or newCol >= cols or grid[newRow][newCol] == 1:
                    continue
                else:
                    yield (newRow,newCol)
        
        def sink (row, col):
            q = [(row,col)]
            flag = True
            while q:
                row,col = q.pop(0)
                if row == 0 or row == rows -1 or col == 0 or col == cols - 1:
                        flag = False
                grid[row][col] = 1 
                for newRow,newCol in nextMove(row,col):
                    q.append((newRow,newCol))
            return flag

        count = 0
        for i in range (rows):
            for j in range (cols):
                if grid[i][j] == 0 and sink(i,j):
                    count += 1
        return count

# Time complexity is O(N * M)

# Space complexity is O(N * M) 