# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

 

# Example 1:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
# Output: 3

# Example 2:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
# Output: 1

 

# Constraints:

#     1 <= wordsDict.length <= 3 * 104
#     1 <= wordsDict[i].length <= 10
#     wordsDict[i] consists of lowercase English letters.
#     word1 and word2 are in wordsDict.
#     word1 != word2

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        words = [word1,word2]
        flag = ''
        idx = 0
        res = float('inf')
        for i in range(len(wordsDict)-1,-1,-1):
            if wordsDict[i] in words and flag and wordsDict[i] != flag:
                res = min(res,idx - i) 
                flag = wordsDict[i]
                idx = i
            elif wordsDict[i] in words and not flag:
                flag = wordsDict[i]
                idx = i
            
            elif wordsDict[i] in words and flag and wordsDict[i] == flag:
                idx = i
             
        return res 

# Time complexity is O(N)

# Space complexity is O(1)