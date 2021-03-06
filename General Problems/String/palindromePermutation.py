# Given a string s, return true if a permutation of the string could form a palindrome.

 

# Example 1:

# Input: s = "code"
# Output: false

# Example 2:

# Input: s = "aab"
# Output: true

# Example 3:

# Input: s = "carerac"
# Output: true

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = Counter(s)   
        count = 0
        for value in counts.values():
            count += value % 2
        return count <= 1

# Time complexity is O(N)

# Space complexity is O(1)