# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.

# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

 

# Constraints:

#     1 <= n <= 104

# BFS solution

class Solution:
    def numSquares(self, n: int) -> int:
        
        def squares(num):
            for i in range(1,int(math.sqrt(n) + 1)):
                if i*i <= num:
                    yield i*i
                    
        queue = collections.deque()
        queue.append((n,0))
        visited = set()
        
        while queue:
            sum,count = queue.popleft()
            if sum == 0:
                return count
            if sum in visited:
                continue
            
            for i in squares(sum):
                queue.append((sum-i,count+1))
                visited.add(sum)

# DP solution. Similar logic to fibonacci dp solution

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = [i**2 for i in range(1,int(math.sqrt(n)) + 1)]
        
        dp = [float('inf')] * (n+1)
        
        dp[0] = 0
        
        for i in range(1,n+1):
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
                
        return dp[-1]

# Time complexity is O(N * sqrt(N))

# Space complexity O(N) for the dp subarray