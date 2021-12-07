# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true

# Example 2:

# Input: s = "foo", t = "bar"
# Output: false

# Example 3:

# Input: s = "paper", t = "title"
# Output: true

 

# Constraints:

#     1 <= s.length <= 5 * 104
#     t.length == s.length
#     s and t consist of any valid ascii character.



class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 ={}
        map2 = {}
        
        for char1,char2 in zip(s,t):
            if(char1 not in map1) and (char2 not in map2):
                map1[char1] = char2
                map2[char2] = char1
                
            elif map1.get(char1) != char2 or map2.get(char2) != char1:
                return False
        return True

# Time complexity is O(N)

# Space complexity is O(1) since the size of the ASCII char set is fixed