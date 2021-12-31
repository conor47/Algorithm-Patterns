# The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

# A chess knight can move as indicated in the chess diagram below:

class Solution:
    def knightDialer(self, n: int) -> int:
        MAX = pow(10,9) + 7
        neighbours = {
            0:(4,6),
            1:(6,8),
            2:(7,9),
            3:(4,8),
            4:(0,3,9),
            5:(),
            6:(0,1,7),
            7:(2,6),
            8:(1,3),
            9:(2,4)
        }
            
        @lru_cache(None)
        def recurse(key,steps):
            if steps == 0:
                return 1
            if steps == 1:
                return len(neighbours[key])
            res = 0
            for nei in neighbours[key]:
                res += recurse(nei,steps-1)
            return res
        total = 0
        for i in range(10):
            total += recurse(i,n-1)
        return total % MAX
        