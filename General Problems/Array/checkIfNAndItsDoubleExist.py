# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

# More formally check if there exists two indices i and j such that :

#     i != j
#     0 <= i, j < arr.length
#     arr[i] == 2 * arr[j]

 

# Example 1:

# Input: arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

# Example 2:

# Input: arr = [7,1,14,11]
# Output: true
# Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.

# Example 3:

# Input: arr = [3,1,7,11]
# Output: false
# Explanation: In this case does not exist N and M, such that N = 2 * M.

 

# Constraints:

#     2 <= arr.length <= 500
#     -10^3 <= arr[i] <= 10^3

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for index,num in enumerate(arr):
            if self.binarySearch(arr,num * 2,index):
                return True
        return False
        
    def binarySearch(self,arr,val,index):
        left = 0
        right = len(arr) - 1
        while left <= right:
            middle = left + (right-left)//2
            
            if arr[middle] == val and middle != index:
                return True
            elif arr[middle] > val:
                right = middle - 1
            else:
                left = middle + 1
        return False

# Time complexity is O(N Log N)

# Space complexity is O(1)

# Solution using counter 

import collections

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        for num in arr:
            if num == 0:
                if count[num * 2] > 1:
                    return True
            else:
                if count[num * 2]:
                    return True
        return False

# solution using a hashset

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if num * 2 in seen or num / 2 in seen:
                return True
            seen.add(num)
        return False

# Time complexity is O(N)
# space complexity is O(N)