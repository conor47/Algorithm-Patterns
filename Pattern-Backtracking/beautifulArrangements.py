# Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

#     perm[i] is divisible by i.
#     i is divisible by perm[i].

# Given an integer n, return the number of the beautiful arrangements that you can construct.

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: 
# The first beautiful arrangement is [1,2]:
#     - perm[1] = 1 is divisible by i = 1
#     - perm[2] = 2 is divisible by i = 2
# The second beautiful arrangement is [2,1]:
#     - perm[1] = 2 is divisible by i = 1
#     - i = 2 is divisible by perm[2] = 1

# Example 2:

# Input: n = 1
# Output: 1

 

# Constraints:

#     1 <= n <= 15

class Solution:
    def countArrangement(self, n: int) -> int:
        ans = 0
        checked = [False for _ in range(1,n+1)]
        
        def backtrack(cand):
            if len(cand) == n:
                nonlocal ans
                ans += 1
                return
            for num in range(1,n+1):
                i = len(cand) + 1
                if checked[num - 1] == False and (num % i ==0 or i % num ==0):
                    checked[num - 1] = True
                    cand.append(num)
                    backtrack(cand)
                    cand.pop()
                    checked[num - 1] = False
        backtrack([])
        return ans

# Time complexity is O(k) where K is the number of valid permutations

# Space complexity is O(n) for the visited array and for the recursion stack