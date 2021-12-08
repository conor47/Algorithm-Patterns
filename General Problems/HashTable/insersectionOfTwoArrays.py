# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

 

# Constraints:

#     1 <= nums1.length, nums2.length <= 1000
#     0 <= nums1[i], nums2[i] <= 1000

 

# Follow up:

#     What if the given array is already sorted? How would you optimize your algorithm?
#     What if nums1's size is small compared to nums2's size? Which algorithm is better?
#     What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?



class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1 = {}
        counts2 = {}
        for num in nums1:
            counts1[num] = counts1.setdefault(num,0) + 1
        for num in nums2:
            counts2[num] = counts2.setdefault(num,0) + 1 
        res = []
        
        for num in counts1:
            if num in counts2:
                m = min(counts1[num], counts2[num])
                res.extend([num] * m) 
        return res
        
        

# Time complexity is O(N + M) where N and M are the lenghts of the input arrays

# Space complexity is O(1) since each hashmap contains at most 10 numbers 

# Some small memory and time complexity optimisations. Use one hash map and iterate across the smaller array

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < len(nums1):
            return self.intersect(nums2,nums1)
        counts = {}
        for num in nums1:
            counts[num] = counts.setdefault(num,0) + 1
        res = []
        
        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] = counts[num] - 1
        return res

# If the arrays were sorted we could use two pointers to iterate through both simultaneously. We increment the smaller pointer until we find
# a match 