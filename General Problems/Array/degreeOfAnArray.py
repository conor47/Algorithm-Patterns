# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

 

# Example 1:

# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.

# Example 2:

# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

 

# Constraints:

#     nums.length will be between 1 and 50,000.
#     nums[i] will be an integer between 0 and 49,999.

# first naieve solution

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = Counter(nums)
        m = float('-inf')
        m = max(counts.values()) 
        cands = [i for i in counts if counts[i] == m]
        res = float('inf')
        for cand in cands:
            res = min(res,self.find(nums,cand))
        return res
            
    def find(self,nums,n):
        
        left = 0
        right = len(nums) - 1
        while nums[left] != n or nums[right] != n:
            if nums[left] != n:
                left +=1
            if nums[right] != n:
                right -=1 
        return right - left + 1

# Time complexity O(N^2)

# Space complexity is (N)