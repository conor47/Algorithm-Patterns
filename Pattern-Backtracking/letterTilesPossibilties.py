# You have n  tiles, where each tile has one letter tiles[i] printed on it.

# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

# Example 1:

# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

# Example 2:

# Input: tiles = "AAABBC"
# Output: 188

# Example 3:

# Input: tiles = "V"
# Output: 1

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set() 
        used = [False] * len(tiles)
        seen = set()
        
        def backtrack(cand):
            nonlocal res
            if cand:
                res.add(cand)
            for i in range(len(used)):
                if not used[i]:
                    cand += tiles[i]
                    used[i] = True
                    backtrack(cand)
                    used[i] = False
                    cand = cand[:-1]
        
        backtrack('')
        return len(res)