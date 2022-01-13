# Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

# A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

 

# Example 1:

# Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

# Example 2:

# Input: words = ["cat","dog","catdog"]
# Output: ["catdog"]

 

# Constraints:

#     1 <= words.length <= 104
#     0 <= words[i].length <= 1000
#     words[i] consists of only lowercase English letters.
#     0 <= sum(words[i].length) <= 105

class Solution:
    
    def __init__ (self):
        self.root = TrieNode()
     
    def insert(self,word):
        cur = self.root
        for char in word:
            cur = cur.children[char]
        cur.isWord = True
    
    @lru_cache(None)
    def find(self,word):
        if len (word) == 0:
            return 1
        count = 0
        cur = self.root
        for idx,char in enumerate(word):
            if char not in cur.children:
                return count 
            cur = cur.children[char]
            if cur.isWord:
                count += self.find(word[idx+1:])
        return count
                      
                
        return False 
        
    
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        for word in words:
            self.insert(word)
        
        res = []
        for word in words:
            if self.find(word) >1:
                res.append(word)
        return res
