# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

# Example 2:

# Input: jewels = "z", stones = "ZZ"
# Output: 0

 

# Constraints:

#     1 <= jewels.length, stones.length <= 50
#     jewels and stones consist of only English letters.
#     All the characters of jewels are unique.

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        chars = {}
        res = 0
        for i in jewels:
            chars[i] = 1
            
        for i in stones:
            if i in chars:
                res +=1
        return res

# Time complexity is O(M + N) where M and N are the lengths of the input strings

# Space complexity is O(M) for the dict 