# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0

 

# Constraints:

#     3 <= nums.length <= 1000
#     -1000 <= nums[i] <= 1000
#     -104 <= target <= 104

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best = [float('inf'),0]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.findSum(nums,i,best,target)
        return best[1]
            
        
    def findSum(self,nums,index,best,target):
        left = index+1
        right = len(nums) - 1
        while left < right:
            s = nums[left] + nums[right] + nums[index]
            if abs(target - s) < best[0]:
                best[0],best[1] = abs(target-s),s
                
            if nums[left] + nums[right] + nums[index] == target:
                break
            
            if nums[left] + nums[right] +nums[index] < target:
                left += 1
            else:
                right -= 1

# Time complexity is O(N^2)

# Space complexity is O(1)

# Cleaner two pointer implementation

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff