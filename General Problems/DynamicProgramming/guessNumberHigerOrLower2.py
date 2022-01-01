# We are playing the Guessing Game. The game will work as follows:

#     I pick a number between 1 and n.
#     You guess a number.
#     If you guess the right number, you win the game.
#     If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
#     Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.

# Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        @lru_cache(None)
        def recurse(l,r):
            if l >= r:
                return 0
            res = float('inf')
            for mid in range(l,r+1):
                res = min(res,mid + max(recurse(mid+1,r),recurse(l,mid-1)))
            return res
        
        return recurse(1,n)

# Time complexity is O(2^n)

# Space complexity is O(N)