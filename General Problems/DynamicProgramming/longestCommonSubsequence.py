# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

#     For example, "ace" is a subsequence of "abcde".

# A common subsequence of two strings is a subsequence that is common to both strings.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.

 

# Constraints:

#     1 <= text1.length, text2.length <= 1000
#     text1 and text2 consist of only lowercase English characters.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1,n2 = len(text1),len(text2)
        dp = [[-1 for _ in range (n2)] for _ in range (n1)]
        return self.lcs(text1,text2,0,0,dp)
    
    def lcs(self,s1,s2,idx1,idx2,dp):
        if idx1 == len(s1) or idx2 == len(s2):
            return 0
        
        
        
        if dp[idx1][idx2] == -1:
            if s1[idx1] == s2[idx2]:
                dp[idx1][idx2]  = 1 + self.lcs(s1,s2,idx1+1,idx2+1,dp)
            else:
                c1 = self.lcs(s1,s2,idx1+1,idx2,dp)
                c2 = self.lcs(s1,s2,idx1,idx2+1,dp)
                dp[idx1][idx2] = max(c1,c2)
        return dp[idx1][idx2]
    
# Time complexity is O(M + N)

# Space complexity is O( M + N)