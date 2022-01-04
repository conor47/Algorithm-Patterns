# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

# Return the number of distinct islands.

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        def isUnique():
            for other in unique_islands:
                if len(other) != len(current_island):
                    continue
                for cell1,cell2 in zip(current_island,other):
                    if cell1 != cell2:
                        break
                else:
                    return False
            return True
        
        def dfs(row,col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if (row,col) in seen or not grid[row][col]:
                return
            seen.add((row,col))
            current_island.append((row_origin-row,col_origin-col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            
        seen = set() 
        unique_islands = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                current_island = []
                row_origin = row
                col_origin = col
                dfs(row,col)
                if not current_island or not isUnique():
                    continue
                else:
                    unique_islands.append(current_island)
        return len(unique_islands)

# Time complexity is O(N^2 * M^2)

# Space complexity is O(N * M)
