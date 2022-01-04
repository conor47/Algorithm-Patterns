# Given a matrix and a target, return the number of non-empty submatrices that sum to target.

# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

# class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        h,w = len(matrix), len(matrix[0])
        
        for i in range(h):
            for j in range(1,w):
                matrix[i][j] = matrix[i][j] + matrix[i][j-1]
        
        res = 0 
        for col1 in range(w):
            for col2 in range(col1,w):
                count = {0:1} 
                acc = 0
                for row in range(h):
                    if col1 == 0:
                        acc += matrix[row][col2]
                    else:
                        acc += matrix[row][col2] - matrix[row][col1 -1]
                    
                    res += count.get(acc - target,0)
                    
                    count[acc] = count.get(acc,0) + 1
        return res

# Time complexity is O(w^2 * h) where w and h are the width and heigh of the matrix