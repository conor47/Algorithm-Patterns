# Given an array, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

 

# Constraints:

#     1 <= nums.length <= 105
#     -231 <= nums[i] <= 231 - 1
#     0 <= k <= 105

# first naieve solution

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        steps = k % len(nums)
        
        temp = nums[-steps:]
        del nums[-steps:]
        
        for i in temp[::-1]:
            nums.insert(0,i)

# Brute force solution

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
    
        
        for i in range(k):
            prev = nums[-1]
        
            for k in range(len(nums)):
                nums[k],prev = prev, nums[k]
            
# Time complexity is O(N * K)

# Space complexity is O(1)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        temp = [0] * n
        
        for i in range (n):
            temp[(i+k) % n] = nums[i]
        nums[:] =temp

# Time complexity is O(N). we use an additional array and in a single pass place every element in its correct position

# Space complexity is O(N)

