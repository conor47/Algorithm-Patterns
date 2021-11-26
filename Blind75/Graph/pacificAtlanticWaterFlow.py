# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

import collections

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        num_rows, num_cols = len(heights), len(heights[0])
        
        pacific_queue = collections.deque()
        atlantic_queue = collections.deque()
        
        for i in range(num_rows):
            pacific_queue.append((i,0))
            atlantic_queue.append((i,num_cols - 1))
        for i in range(num_cols):
            pacific_queue.append((0,i))
            atlantic_queue.append((num_rows-1,i))
            
        def BFS(queue):
            reachable = set()
            
            while queue:
                (row,col) = queue.popleft()
                
                reachable.add((row,col))
                
                for (x,y) in [(1,0),(0,1),(-1,0),(0,-1)]:
                    new_row = row + x
                    new_col = col + y
                    
                    if new_row < 0 or new_row >= num_rows or new_col <0 or new_col >= num_cols:
                        continue
                    
                    if(new_row,new_col) in reachable:
                        continue
                        
                    if heights[new_row][new_col] < heights[row][col]:
                        continue
                        
                    queue.append((new_row,new_col))
            return reachable
        
        pacific_reachable = BFS(pacific_queue)
        atlantic_reachable = BFS(atlantic_queue)
        
        return list(pacific_reachable.intersection(atlantic_reachable))
    
# Time complexity is O(M * N). In the worst case we have to visit each cell twice

# Space complexity is O( M * N)