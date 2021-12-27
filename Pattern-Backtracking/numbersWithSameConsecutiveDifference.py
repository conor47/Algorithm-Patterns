# Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

# Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

# You may return the answer in any order.

 

# Example 1:

# Input: n = 3, k = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.

# Example 2:

# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

 

# Constraints:

#     2 <= n <= 9
#     0 <= k <= 9

# Original DFS solution

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        seen = set()  
        
        def backtrack(num):
            if len(str(num)) == n and num not in seen:
                seen.add(num)
                res.append(num)
                return
            elif len(str(num)) == n:
                return
            elif num and int(str(num)[0]) == 0:
                return
            for new in nextNum(num,k):
                backtrack(new)
             
            
        def nextNum(num,k):
            last = int(str(num)[-1])
            diff = (k,-k)
            for d in diff:
                temp = num
                if 0 <= last + d <= 9:
                    temp = str(num) + str(last + d)
                    yield(int(temp))
        
        for i in range(1,10):
            backtrack(i)
        return res

# Better DFS solution

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        
        def dfs(num,n):
            if n == 0:
                res.append(num)
                return
            
            tail = num % 10
            
            next_digits = set([tail + k, tail - k])
            for next_digit in next_digits:
                if 0<= next_digit <= 9:
                    new_num = num * 10 + next_digit
                    dfs(new_num,n - 1)
         
        for i in range(1,10):
            dfs(i,n-1)
        return res

# Time complexity is O(2^N). The execution of the algo will unfold itself as a binary tree. In the worst case the number of nodes in binary tree
# of deptb N - 1 is 2^n

# Space complexity is O(2^n). The recursion stack will take O(N