# Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

 

# Example 1:

# Input: nums = [1,-1,5,-2,3], k = 3
# Output: 4
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

# Example 2:

# Input: nums = [-2,-1,2,1], k = 1
# Output: 2
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.

 

# Constraints:

#     1 <= nums.length <= 2 * 105
#     -104 <= nums[i] <= 104
#     -109 <= k <= 109



class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = longest = 0
        
        indices = {}
        
        for i,num in enumerate(nums):
            prefix_sum += num
            
            if prefix_sum == k:
                longest = max(longest,i+1)
            
            if prefix_sum - k in indices:
                longest = max(longest,i - indices[prefix_sum - k])
            
            if prefix_sum not in indices:
                indices[prefix_sum ] = i
        return longest

# Time complexity is O(N)

# Space complexity is O(N)