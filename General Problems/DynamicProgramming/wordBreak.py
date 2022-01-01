# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

 

# Constraints:

#     1 <= s.length <= 300
#     1 <= wordDict.length <= 1000
#     1 <= wordDict[i].length <= 20
#     s and wordDict[i] consist of only lowercase English letters.
#     All the strings of wordDict are unique.

class solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        n = len(s)
        for i in range(n-1,-1,-1):
            for word in wordDict:
                if i + len(word) <= len(s) and word == s[i:i + len(word)]:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return dp[0]

# Time complexity is O(N * M) where m is the number of words in the word dict

# Space complexity is O(N)