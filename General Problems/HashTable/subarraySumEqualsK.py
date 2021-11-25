# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

 

# Constraints:

#     1 <= nums.length <= 2 * 104
#     -1000 <= nums[i] <= 1000
#     -107 <= k <= 107

# Accepted
# 613,281
# Submissions
# 1,402,339

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = {}
        count = 0
        sum = 0
        counts[0] = 1
        for i in range (len(nums)):
            sum += nums[i]
            if sum - k in counts:
                count += counts[sum-k]
            if sum in counts:
                counts[sum] = counts[sum] + 1
            else:
                counts[sum] = 1
        return count

# Time complexity is O(N)

# Space complexity is O(N)
