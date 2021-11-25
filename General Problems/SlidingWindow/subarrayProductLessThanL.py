# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

# Example 2:

# Input: nums = [1,2,3], k = 0
# Output: 0

 

# Constraints:

#     1 <= nums.length <= 3 * 104
#     1 <= nums[i] <= 1000
#     0 <= k <= 106



class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        start = 0
        end = 0
        product = 1
        count = 0
        while end < len(nums):
            product *= nums[end]
            if product < k:
                count += end - start + 1
                end += 1
            else:
                while product >= k and start <= end:
                    product /= nums[start]
                    start +=1
                count += end - start + 1
                end += 1
        return count

# Time complexity is O(N)

# Space complexity is O(1)