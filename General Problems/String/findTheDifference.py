# You are given two strings s and t.

# String t is generated by random shuffling string s and then add one more letter at a random position.

# Return the letter that was added to t.

 

# Example 1:

# Input: s = "abcd", t = "abcde"
# Output: "e"
# Explanation: 'e' is the letter that was added.

# Example 2:

# Input: s = "", t = "y"
# Output: "y"

# Example 3:

# Input: s = "a", t = "aa"
# Output: "a"

# Example 4:

# Input: s = "ae", t = "aea"
# Output: "a"

 

# Constraints:

#     0 <= s.length <= 1000
#     t.length == s.length + 1
#     s and t consist of lower-case English letters.

from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts = Counter(s)
        
        for char in t:
            if counts[char] == 0 or not counts[char]:
                return char
            counts[char] = counts[char] -1 

# Time complexity is O(N)

# Space comlexity is O(1) since the size of our counter is bounded by 26