# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

# Example 1:

# Input: nums = [1,2,2,3]
# Output: true

# Example 2:

# Input: nums = [6,5,4,4]
# Output: true

# Example 3:

# Input: nums = [1,3,2]
# Output: false

 

# Constraints:

#     1 <= nums.length <= 105
#     -105 <= nums[i] <= 105

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        increasing = True        
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                increasing = False
                break
        decreasing = True
        for i in range(n-1):
            if nums[i] < nums[i+1]:
                decreasing = False
                break
        return increasing or decreasing

# Time complexity is O(N)

# Space complexity is O(1)

# Single pass 

class Solution(object):
    def isMonotonic(self, A):
        store = 0
        for i in xrange(len(A) - 1):
            c = cmp(A[i], A[i+1])
            if c:
                if c != store != 0:
                    return False
                store = c
        return True