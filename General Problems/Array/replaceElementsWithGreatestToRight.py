# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.

 

# Example 1:

# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.

# Example 2:

# Input: arr = [400]
# Output: [-1]
# Explanation: There are no elements to the right of index 0.

 

# Constraints:

#     1 <= arr.length <= 104
#     1 <= arr[i] <= 105

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n
        if n == 1:
            return res
        
        for i in range(n):
            if i > 0 and arr[i] < res[i-1]:
                res[i] = res[i-1]
                continue
            m = float('-inf')
            for j in range(i+1,n):
                m = max(m,arr[j])
            res[i] = m
        res[-1] = -1
        return res

# Space complexity is O(N^2)

# Much more efficient solution looping backwards through the array

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        return self.replace(arr)

    def replace(self,arr,mx=-1):
        for i in range(len(arr)-1,-1,-1):
            arr[i],mx = mx,max(mx,arr[i])
        return arr

# Time complexity is O(N)

# Space complexity is O(1)