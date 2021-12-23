# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sideLength = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        if sum(matchsticks) / 4 != sideLength:
            return False
        
        sides = [0,0,0,0]
        
        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= sideLength:
                    sides[j] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
        return backtrack(0)

# Time complexity is O(N^4)

# Space complexity is O(N)