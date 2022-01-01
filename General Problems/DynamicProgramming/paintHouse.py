# There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

#     For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...

# Return the minimum cost to paint all houses.

 

# Example 1:

# Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
# Minimum cost: 2 + 5 + 3 = 10.

# Example 2:

# Input: costs = [[7,6,2]]
# Output: 2

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0 for i in range(3)] for _ in range(n)]
        
        for i in range(3):
            dp[0][i] = costs[0][i]
        
        for i in range(1,n):
            for j in range(3):
                dp[i][j] = costs[i][j] + min(dp[i-1][(j-1) % 3],dp[i-1][(j+1) % 3])
        return min(dp[n-1])
    
# Time complexity is O(N)

# Space complexity is O(N)