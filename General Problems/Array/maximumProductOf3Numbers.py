# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: 6

# Example 2:

# Input: nums = [1,2,3,4]
# Output: 24

# Example 3:

# Input: nums = [-1,-2,-3]
# Output: -6

 

# Constraints:

#     3 <= nums.length <= 104
#     -1000 <= nums[i] <= 1000

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        cand1 = nums[0] * nums[1] * nums[2]
        cand2 = nums[0] * nums[1] * nums[-1]
        cand3 = nums[-1] * nums[-2] * nums[-3]
        return max(cand1,cand2,cand3)

# Time complexity is O(N Log N)

# Space complexity is O(N) or O(1) depending on the sorting algo used