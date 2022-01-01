# You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).

# Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps. Since the answer may be too large, return it modulo 109 + 7.

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MAX = pow(10,9) + 7
        
        @lru_cache(None)
        def recurse(steps,idx):
            if idx < 0 or idx >= arrLen:
                return 0
            if steps == 0:
                return 1 if idx == 0 else 0
            directions = (-1,0,1)
            res = 0
            for dx in directions:
                res += recurse(steps-1,idx+dx)
            return res
        return recurse(steps,0) % MAX

