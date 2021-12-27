# An n-bit gray code sequence is a sequence of 2n integers where:

#     Every integer is in the inclusive range [0, 2n - 1],
#     The first integer is 0,
#     An integer appears no more than once in the sequence,
#     The binary representation of every pair of adjacent integers differs by exactly one bit, and
#     The binary representation of the first and last integers differs by exactly one bit.

# Given an integer n, return any valid n-bit gray code sequence.

 

# Example 1:

# Input: n = 2
# Output: [0,1,3,2]
# Explanation:
# The binary representation of [0,1,3,2] is [00,01,11,10].
# - 00 and 01 differ by one bit
# - 01 and 11 differ by one bit
# - 11 and 10 differ by one bit
# - 10 and 00 differ by one bit
# [0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
# - 00 and 10 differ by one bit
# - 10 and 11 differ by one bit
# - 11 and 01 differ by one bit
# - 01 and 00 differ by one bit

# Example 2:

# Input: n = 1
# Output: [0,1]

 

# Constraints:

#     1 <= n <= 16



class Solution:
    def grayCode(self, n: int) -> List[int]:
        nums = [i for i in range(pow(2,n))]
        used = set()
        used.add(0)
        res = [0]
         
        def backtrack(res,used,n):
            if len(res) == (1 << n):
                return True
            
            current = res[-1]
            for i in range(n):
                next = current ^ (1 << i)
                if next not in used:
                    used.add(next)
                    res.append(next)
                    if(backtrack(res,used,n)):
                        return True
                    res.pop() 
                    used.remove(next)
            return False
        
        backtrack(res,used,n)
        return res

# Time complexity is O(2^n)!. With N bits there are 2^n possible numebrs 

# Space complexity is O(2^n) for the used set. The max depth of the recursion stack is 2^n