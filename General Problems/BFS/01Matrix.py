# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

# Basic bsf solution. TLEs on leetcodes last test case. bfs starts from each 1 in the matrix

import collections

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        res = [[0 for _ in range(cols)] for _ in range(rows)]
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        def helper(row,col):
            for x,y in directions:
                new_row = row+x
                new_col = col+y
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                    continue
                yield (new_row,new_col)
        
        for i in range (rows):
            for j in range (cols):
                if mat[i][j] == 0:
                    continue
                visited = set()
                queue = collections.deque()
                queue.append((i,j,0))
                visited.add((i,j))
                dist = 0
                
                while queue:
                    row,col,distance = queue.popleft()
                    visited.add((row,col))
                    if mat[row][col] == 0:
                        dist = distance
                        break
                    for new_row,new_col in helper(row,col):
                        if (new_row,new_col) not in visited:
                            queue.append((new_row,new_col,distance+1))
                res[i][j] = dist
        return res

# Time complexity is O(NM ^ 2). We potentially iterate over the entire matrix for each 1 in the matrix

# Space complexity is O(NM)

# solution using bfs from each 0 in the matrix

import collections

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        res = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        def helper(row,col):
            for x,y in directions:
                new_row = row+x
                new_col = col+y
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                    continue
                yield (new_row,new_col)
        
        queue = collections.deque()
        for i in range (rows):
            for j in range (cols):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    queue.append((i,j))
                    
        while queue:
            row,col = queue.popleft()
            
            for new_row,new_col in helper(row,col):
                if res[new_row][new_col] > res[row][col]:
                    res[new_row][new_col] = res[row][col] + 1
                    queue.append((new_row,new_col))
        return res