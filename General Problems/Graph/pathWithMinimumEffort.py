# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        
        diff = [[float('inf')]*cols for _ in range(rows)]
        diff[0][0] = 0
        visited = [[False]*cols for _ in range(rows)]
        
        heap = [(0,0,0)]
        
        while heap:
            difference,x,y = heapq.heappop(heap)
            
            visited[x][y] = True
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            
            for dx,dy in directions:
                row,col = x + dx, y + dy
                
                if 0<= row < rows and 0<= col < cols and not visited[row][col]:
                    current_dif = abs(heights[row][col] - heights[x][y])
                    max_dif = max(current_dif,diff[x][y])
                    
                    if diff[row][col] > max_dif:
                        diff[row][col] = max_dif
                        heapq.heappush(heap,(max_dif,row,col))
        return diff[-1][-1]

# Time complexity is O(N*M * Log NM). Since there can be at most N*M items in the heap, each pop and push operation can take up to Log NM time

# Space complexity is O(N*M)