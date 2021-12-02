# Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

#     Integers in each row are sorted in ascending from left to right.
#     Integers in each column are sorted in ascending from top to bottom.


# The brute force solution is to search the entire matrix cell by cell. Takes O(NM) time

# Binary search over rows or columns 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        
        for i in range (n):
            start = 0;
            end = m-1
            while start <=end:
                middle = start + (end - start )//2
                if matrix[i][middle] == target:
                    return True
                elif matrix[i][middle] < target:
                    start = middle + 1
                else:
                    end = middle - 1
        return False

# Time complexity is O(N LogM)
# Space complexity is O(1)

# search space reduction solution

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        n = len(matrix)
        m = len(matrix[0])
        
        row = n-1
        col = 0
        
        while col < m and row >=0:
            
            if matrix[row][col] == target:
                return True
            
            if matrix[row][col] > target:
                row -= 1
            
            else:
                col += 1
                
        return False

# Time complexity is O(N * M)
# Space complexity is O(1)