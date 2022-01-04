# Given an integer array nums, handle multiple queries of the following type:

#     Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

# Implement the NumArray class:

#     NumArray(int[] nums) Initializes the object with the integer array nums.
#     int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

 

# Example 1:

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixSum = [nums[0]]
        for i in range(1,len(nums)):
            self.prefixSum.append(self.prefixSum[i-1] + nums[i]) 

    def sumRange(self, left: int, right: int) -> int:
        if left == right:
            return self.nums[left]
        elif left == 0:
            return self.prefixSum[right]
        else:
            return self.prefixSum[right] - self.prefixSum[left-1]

# Time complexity of initialisation is O(N). Time complexity of each query is O(1)

# Space complexity is O(N)