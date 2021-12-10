# Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

# Note that the letters wrap around.

#     For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.

 

# Example 1:

# Input: letters = ["c","f","j"], target = "a"
# Output: "c"

# Example 2:

# Input: letters = ["c","f","j"], target = "c"
# Output: "f"

# Example 3:

# Input: letters = ["c","f","j"], target = "d"
# Output: "f"

# Example 4:

# Input: letters = ["c","f","j"], target = "g"
# Output: "j"

# Example 5:

# Input: letters = ["c","f","j"], target = "j"
# Output: "c"

 

# Constraints:

#     2 <= letters.length <= 104
#     letters[i] is a lowercase English letter.
#     letters is sorted in non-decreasing order.
#     letters contains at least two different characters.
#     target is a lowercase English letter.

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = self.binarySearch(letters,target)
        n = len(letters)
        return letters[(idx)%n]
        
    
    
    def binarySearch(self,arr, target):
        left = 0
        right = len(arr) -1 
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

# Time complexity is O(Log N)
# Space complexity is O(1)