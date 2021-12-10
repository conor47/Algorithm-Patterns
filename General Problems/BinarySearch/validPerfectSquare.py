# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Follow up: Do not use any built-in library function such as sqrt.

 

# Example 1:

# Input: num = 16
# Output: true

# Example 2:

# Input: num = 14
# Output: false

 

# Constraints:

#     1 <= num <= 2^31 - 1

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left = 1
        right = num // 2 
        
        while left <= right:
            mid = left + (right - left)//2 
            val = mid * mid
            if val == num:
                return True
            elif val > num:
                right = mid - 1
            else:
                left = mid + 1
        return False

# Time complexity is O(Log N)

# Space complexity is O(1)