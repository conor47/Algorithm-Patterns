# he pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

#     For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.

# Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

#     Each element of nums is in exactly one pair, and
#     The maximum pair sum is minimized.

# Return the minimized maximum pair sum after optimally pairing up the elements.

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        m = float('-inf')
        while left < right:
            m = max(m,nums[left] + nums[right])
            left += 1
            right -= 1
        return m

# Time complexity is O(N Log N)

# Space complexity is O(N) if the sorting algorithm uses extra space. Otherwise O(1)