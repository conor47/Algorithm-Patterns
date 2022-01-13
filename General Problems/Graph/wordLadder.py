# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

#     Every adjacent pair of words differs by a single letter.
#     Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#     sk == endWord

# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

 

# Constraints:

#     1 <= beginWord.length <= 10
#     endWord.length == beginWord.length
#     1 <= wordList.length <= 5000
#     wordList[i].length == beginWord.length
#     beginWord, endWord, and wordList[i] consist of lowercase English letters.
#     beginWord != endWord
#     All the words in wordList are unique.



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

# Time complexity O(M^2 * N) where M is the length of the words in the list and N is the number of words. We iterate over each N words
# and for each word we iterate over it generating its intermediate states. This string operation takes O(M) time this leading us to a 
# Time complexity of (M^2 * N). The BFS is also O(M^2 * N)

# Space complexity is O(M^2 * N). For each itermediate state of each word we save it as a key and it word as a value. For each word there
# are M possible intermediate states leading us to a time complexity of O(M^2 * N) 