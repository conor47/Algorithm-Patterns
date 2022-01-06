# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A good array is an array where the number of different integers in that array is exactly k.

#     For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

# Example 2:

# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

 

# Constraints:

#     1 <= nums.length <= 2 * 104
#     1 <= nums[i], k <= nums.length

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMost(k):
            counts = {}
            res = i = 0
            for j in range(len(nums)):
                if nums[j] not in counts:
                    k -= 1
                    counts[nums[j]] = 1 
                else:
                    counts[nums[j]] = counts[nums[j]] + 1
                while k < 0:
                    counts[nums[i]] = counts[nums[i]] - 1
                    if counts[nums[i]] == 0:
                        del counts[nums[i]]
                        k += 1
                    i += 1
                res += j - i + 1
            return res
          
        return atMost(k) - atMost(k-1)

# Time complexity is O(N)

# Spaec complexity is O(K)