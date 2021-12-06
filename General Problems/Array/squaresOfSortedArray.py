# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

 

# Constraints:

#     1 <= nums.length <= 104
#     -104 <= nums[i] <= 104
#     nums is sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x*x for x in nums)

# Time complexity is O(N LogN)
# Space complexity is O(Log N) or O(N) depending on the languages sorting function

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        
        left = 0
        right = len(nums) - 1
            
        while left <=right:
            leftSquare = nums[left] * nums[left]
            rightSquare = nums[right] * nums[right]
            
            if leftSquare > rightSquare:
                res.insert(0,leftSquare)
                left += 1
            elif rightSquare > leftSquare:
                res.insert(0,rightSquare)
                right -= 1
            else:
                res.insert(0,leftSquare)
                left += 1
        return res

# Time complexity is O(N)
# Space complexity O(N) if we count the result array, O(1) otherwise