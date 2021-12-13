# The power of the string is the maximum length of a non-empty substring that contains only one unique character.

# Given a string s, return the power of s.

 

# Example 1:

# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.

# Example 2:

# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

# Example 3:

# Input: s = "triplepillooooow"
# Output: 5

# Example 4:

# Input: s = "hooraaaaaaaaaaay"
# Output: 11

# Example 5:

# Input: s = "tourist"
# Output: 1

 

# Constraints:

#     1 <= s.length <= 500
#     s consists of only lowercase English letters.

class Solution:
    def maxPower(self, s: str) -> int:
        power = 1
        count = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1
                power = max(count,power)
            else:
                count = 1
        return power

# Time complexity is O(N) where N is length of the input string

# Space complexity is O(1)

