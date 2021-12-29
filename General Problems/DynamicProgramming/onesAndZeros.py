# You are given an array of binary strings strs and two integers m and n.

# Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

# A set x is a subset of a set y if all elements of x are also elements of y.

 

# Example 1:

# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

# Example 2:

# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: The largest subset is {"0", "1"}, so the answer is 2.

 

# Constraints:

#     1 <= strs.length <= 600
#     1 <= strs[i].length <= 100
#     strs[i] consists only of digits '0' and '1'.
#     1 <= m, n <= 100

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = {}
        for s in strs:
            counts[s] = Counter(s)
        
        @lru_cache(maxsize = None)
        def recursive(x,y,index,res):
            if index == len(strs) :
                return res
            
            chars = counts[strs[index]] 
            x += chars['0']
            y += chars['1']
            s1 = 0
            if y <=n and x <= m:
                s1 = recursive(x,y,index+1,res+1)
            x -= chars['0']
            y -= chars['1']
            s2 = recursive(x,y,index+1,res)
            return max(s1,s2)
        
        return recursive(0,0, 0, 0)
                # First naieve solution

                
# Time complexity is O(l * m * n)

# space complexity is O(l * m * n) used for memoization