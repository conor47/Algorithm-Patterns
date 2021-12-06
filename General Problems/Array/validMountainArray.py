# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

#     arr.length >= 3
#     There exists some i with 0 < i < arr.length - 1 such that:
#         arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#         arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        left = 0
        right = len(arr) - 1
        
        while left < right and arr[left+1] > arr[left] :
                left += 1
        while right > left and arr[right-1] > arr[right]:
                right -= 1
                
        return left == right and left != 0 and right != (len(arr) - 1)

# Time complexity is O(N)
# Space complexity is O(1)

