# Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

 

# Example 1:

# Input: nums = [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.

# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 4

 

# Constraints:

#     1 <= nums.length <= 105
#     nums[i] is either 0 or 1.

 

# Follow up: What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLen = 0
        onesCount = 0
        windowStart = 0
        
        for windowEnd in range(0,len(nums)):
            if nums[windowEnd] == 1:
                onesCount += 1
            
            if (windowEnd - windowStart + 1 - onesCount > 1):
                if nums[windowStart] == 1:
                    onesCount -= 1
                windowStart += 1
            maxLen = max(maxLen, windowEnd - windowStart + 1)
        return maxLen

# Time complexity is O(N)

# Space complexity is O(1)