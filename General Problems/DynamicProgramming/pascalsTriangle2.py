# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        temp = [1]
        
        for i in range(1,rowIndex+1):
            row = [0] * (i+1)
            row[0],row[-1] = 1,1
            
            for col in range(1,len(row)-1):
                row[col] = temp[col-1] + temp[col]
            temp = row
        return temp

# Time complexity is O(k^2) 

# Space complexity O(K)