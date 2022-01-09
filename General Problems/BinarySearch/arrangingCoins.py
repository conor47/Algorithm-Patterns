# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 1
        for i in range(1, n):
            if (i*(i+1) // 2) <= n:
                res = i
            else:
                break
        return res 

# Time complexity is O(N)

# Space complexity is O(1)

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid =  (left + right) // 2
            cur = mid * (mid+1) // 2
            
            if cur == n:
                return mid
            if cur > n:
                right = mid
            else:
                left = mid + 1
        return left - 1 if left != 1 else 1

# Time complexity is O(Log N)

# Space complexity is O(1)