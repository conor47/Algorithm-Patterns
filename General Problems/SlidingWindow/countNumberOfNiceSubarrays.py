# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.

 

# Example 1:

# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

# Example 2:

# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There is no odd numbers in the array.

# Example 3:

# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16

 

# Constraints:

#     1 <= nums.length <= 50000
#     1 <= nums[i] <= 10^5
#     1 <= k <= nums.length

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def count(k):
            res = i = 0
            
            for j in range(len(nums)):
                if nums[j] % 2 != 0:
                    k -= 1
                while k < 0:
                    if nums[i] % 2 != 0:
                        k += 1
                    i += 1
                res += j - i + 1
            return res
        
        return count(k) - count(k-1)

# Time complexity is O(N)

# Space complexity is O(1)