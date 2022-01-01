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
    dp = {0:0,1:1}
    def minDays(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        one = 1 + (n%2) + self.minDays(n//2)
        two = 1 + (n%3) + self.minDays(n//3)
        self.dp[n] = min(one,two)
        return self.dp[n]

# Time complexity is O(Log N)

# Space complexity is O(N)