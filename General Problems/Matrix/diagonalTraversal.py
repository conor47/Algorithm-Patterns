# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        flag = True
        res = []
        for i in range (len(mat[0])):
            temp = self.traverse(mat,0,i)
            if flag:
                res.extend(temp[::-1])
            else:
                res.extend(temp)
            flag = not flag
        for i in range(1,len(mat)):
            temp = self.traverse(mat,i,len(mat[0])-1)
            if flag:
                res.extend(temp[::-1])
            else:
                res.extend(temp)
            flag = not flag
        return res        
    
    def traverse(self,mat,row,col):
        res = []
        while row >= 0 and col >= 0 and row < len(mat) and col < len(mat[0]):
            res.append(mat[row][col])
            row += 1
            col -= 1
        return res

# Time complexity is O(N*M + N*M/2)

# Space complexity is (max(N,M))