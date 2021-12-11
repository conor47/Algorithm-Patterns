# Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

 

# Example 1:

# Input: nums = [-2,0,1,3], target = 2
# Output: 2
# Explanation: Because there are two triplets which sums are less than 2:
# [-2,0,1]
# [-2,0,3]

# Example 2:

# Input: nums = [], target = 0
# Output: 0

# Example 3:

# Input: nums = [0], target = 0
# Output: 0

 

# Constraints:

#     n == nums.length
#     0 <= n <= 3500
#     -100 <= nums[i] <= 100
#     -100 <= target <= 100

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) -2):
            count += self.search(nums,i+1,target - nums[i])
        return count
            
    def search(self,arr,start,target):
        count = 0
        left = start
        right = len(arr) - 1
        while left < right:
            if (arr[left]+arr[right] < target):
                count += right - left
                left += 1
            else:
                right -= 1
        return count

# Time complexity is O(N Log N * N^2) which is O(N^2). Sorting the array and looping through it take N * Log N time and running the 
# search takes N^2 time

# Space complexity is O(1)