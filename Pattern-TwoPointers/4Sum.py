# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

#     0 <= a, b, c, d < n
#     a, b, c, and d are distinct.
#     nums[a] + nums[b] + nums[c] + nums[d] == target

# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

 

# Constraints:

#     1 <= nums.length <= 200
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        def searchPair(first,second):
            third = second + 1
            fourth = len(nums) -1 
            while third < fourth:
                s = nums[first] + nums[second] + nums[third] + nums[fourth]
                if s == target:
                    res.append([nums[first] ,nums[second] , nums[third] , nums[fourth]])
                    third += 1
                    fourth -= 1
                    while third < fourth and nums[third] == nums[third -1]:
                        third += 1
                    while third < fourth and nums[fourth] == nums[fourth + 1]:
                        fourth -= 1
                elif s > target:
                    fourth -= 1
                else:
                    third += 1
               
        if n<4:
            return res
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue    
                searchPair(i,j)
        return res 

# Time complexity is O(N^3)

# Space complexity is O(N) or O(1) for sorting algo