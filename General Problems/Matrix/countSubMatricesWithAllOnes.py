# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

# Example 1:

# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation: 
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.

# Example 2:

# Input: matrix = 
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation: 
# There are 6 squares of side 1.  
# There is 1 square of side 2. 
# Total number of squares = 6 + 1 = 7.

 

# Constraints:

#     1 <= arr.length <= 300
#     1 <= arr[0].length <= 300
#     0 <= arr[i][j] <= 1

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or len(matrix) == 0:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0]) 
        res = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        res += 1
                    else:
                        count = min(matrix[i-1][j],matrix[i-1][j-1],matrix[i][j-1]) + 1
                        res += count
                        matrix[i][j] = count
        return res

# Time complexity is O(N * M) since we are looping over each cell in the matrix

# Space complexity is O(1) since we are modifying the original matrix