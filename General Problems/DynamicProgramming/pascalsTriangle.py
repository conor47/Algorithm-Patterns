# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        for i in range(numRows):
            row = [0] * (i+1)
            row[0],row[-1] = 1,1
            
            for col in range(1,len(row)-1):
                row[col] = res[i-1][col-1] + res[i-1][col]
            res.append(row)
        return res

# Time complexity is O(R^2) where R is the number of rows. We have a nested for loop in which both loops run for numRows iterations.

# Space complexity is O(R^2) since are storing each generated number
