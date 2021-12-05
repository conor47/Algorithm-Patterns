# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

# Example 2:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 3:

# Input: nums = [1,2,3]
# Output: 3

 

# Constraints:

#     1 <= nums.length <= 100
#     0 <= nums[i] <= 1000

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[1], nums[0])
        
        arr1 = nums[1:]
        arr2 = nums[:-1]
        return max(self.robber(arr1), self.robber(arr2))
        
        
    def robber(self,arr):
        dp = [0] * len(arr)
        dp[0],dp[1] = arr[0], max(arr[0],arr[1])
        for i in range (2,len(arr)):
            dp[i] = max(dp[i-1], dp[i-2]+arr[i])
        return dp[-1]
            
# Time complexity O(N)
# Space complexity is O(N)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[1], nums[0])
        
        arr1 = nums[1:]
        arr2 = nums[:-1]
        return max(self.robber(arr1), self.robber(arr2))
        
        
    def robber(self,arr):
        t1 = 0
        t2 = 0
        for house in arr:
            temp = t1
            t1 = max(house+t2,t1)
            t2 = temp
        return t1

# Time complexity is O(N)
# Space complexity is O(1)