# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

# Return the shortest such subarray and output its length.

 

# Example 1:

# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

# Example 2:

# Input: nums = [1,2,3,4]
# Output: 0

# Example 3:

# Input: nums = [1]
# Output: 0

 

# Constraints:

#     1 <= nums.length <= 104
#     -105 <= nums[i] <= 105

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        copy = sorted(nums[:])
        start = 0
        end = len(copy) -1 
        
        while start <= end and (copy[start] == nums[start] or copy[end] == nums[end]):
            if copy[start] == nums[start]:
                start += 1
            
            if copy[end] == nums[end]:
                end -= 1
        
        return end - start + 1 if start < end else 0

# Time complexity is O(NLogN) for sorting

# Space comlpexity is O(N) for the sorting and for the copy of the array

# Stack solution

# We use a stack to determine the left most unsorted element and then the rightmost unsorted element

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        l,r = len(nums),0
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l,stack.pop())
            stack.append(i)
            
        stack = []
        
        for i in range(len(nums) - 1,-1,-1):
            while stack and nums[stack[-1]] < nums[i]:
                r = max(r,stack.pop())
            stack.append(i)
            
        return r - l + 1 if r - l > 0 else 0

# Time complexity is O(N)

# Space complexity is O(N)

