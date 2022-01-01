# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

# In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1_000_000_007
        
        @lru_cache(None)
        def p(n):
            if n == 2:
                return 1
            else:
                return (p(n-1) + f(n-2)) % MOD
        
        @lru_cache(None)
        def f(n):
            if n <= 2:
                return n
            else:
                return (f(n-1) + f(n-2) + 2 * p(n-1)) % MOD
        
        return f(n)

# Time complexity is O(N). There will be N non memoized calls to f and p each of which will take O(N) time. There will be an additional 
# 2N memoized calls to f and 3N memoized calls to p, each of which are constant time.

# Space complexity is O(N) for the recursion stackGiven an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.