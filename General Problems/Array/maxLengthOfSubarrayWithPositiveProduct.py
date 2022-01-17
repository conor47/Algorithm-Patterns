# Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

# A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

# Return the maximum length of a subarray with positive product.

 

# Example 1:

# Input: nums = [1,-2,-3,4]
# Output: 4
# Explanation: The array nums already has a positive product of 24.

# Example 2:

# Input: nums = [0,1,-2,-3,-4]
# Output: 3
# Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
# Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.

# Example 3:

# Input: nums = [-1,-2,-3,0,1]
# Output: 2
# Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].

 

# Constraints:

#     1 <= nums.length <= 105
#     -109 <= nums[i] <= 109



class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        positive, negative = 0,0   
        res = 0
        
        for num in nums:
            
            if num > 0:
                positive += 1
                if negative > 0:
                    negative += 1
                else:
                    negative = 0

                
            elif num == 0:
                positive = 0
                negative = 0
                
            else:
                temp = positive
                if negative > 0:
                    positive = negative + 1
                else:
                    positive = 0
                negative = temp + 1
            
            res = max(positive,res)
        
        return res

# Time complexity is O(N)

# Space complexity is O(1)