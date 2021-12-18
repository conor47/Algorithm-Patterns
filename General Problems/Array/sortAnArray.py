# Given an array of integers nums, sort the array in ascending order.

 

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]

# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]

 

# Constraints:

#     1 <= nums.length <= 5 * 104
#     -5 * 104 <= nums[i] <= 5 * 104

# Merge sort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
                
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left,right)
    
    def merge(self,arr1, arr2):
            res = []
            i, j = 0, 0
            
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    res.append(arr1[i])
                    i+= 1
                elif arr1[i] > arr2[j]:
                    res.append(arr2[j])
                    j += 1
                else:
                    res.append(arr1[i])
                    res.append(arr2[j])
                    i+= 1
                    j += 1
            while i < len(arr1):
                res.append(arr1[i])
                i += 1
            while j < len(arr2):
                res.append(arr2[j])
                j += 1
            return res

# Time complexity is O(N LogN)

# Space complexity is O(N)