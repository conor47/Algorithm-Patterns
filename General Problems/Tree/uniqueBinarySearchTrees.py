# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

# Dynamic programming answer

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        g = [0] * (n+1)
        
        g[0],g[1] = 1,1
        
        for i in range(2,n+1):
            for j in range(1,i+1):
                g[i] += g[j-1] * g[i-j]
        return g[n]

# recursive answer

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1 :
            return 1
        
        ans=0
        for i in range(1,n+1):
            ans += self.numTrees(i-1) * self.numTrees(n-i) 
        return ans

# Time complexity is O(N^3)

# Space complexity is O(N)