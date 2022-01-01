# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

# Return the maximum product you can get.

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.

# Example 2:

# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

 

# Constraints:

#     2 <= n <= 58



class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        
        for num in range(2,n+1):
            dp[num] = 0 if num == n else num
            for j in range(1,num):
                val = dp[j] * dp[num - j]
                dp[num] = max(dp[num],val)
        return dp[n]

# Time complexity is O(N^2)

# Space complexity is O(N)