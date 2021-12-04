# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

#     Trie() Initializes the trie object.
#     void insert(String word) Inserts the string word into the trie.
#     boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
#     boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

 

# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True

 

# Constraints:

#     1 <= word.length, prefix.length <= 2000
#     word and prefix consist only of lowercase English letters.
#     At most 3 * 104 calls in total will be made to insert, search, and startsWith.

class Trie:
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if not node.containsKey(char):
                node.put(char,TrieNode())
            node = node.get(char)
        node.setEnd()
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if not node.containsKey(char):
                return False
            node = node.get(char)
        return node.isEnd()
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if not node.containsKey(char):
                return False
            node = node.get(char)
        return True

# Time complexity of insertion is O(M) where M is the length of the key. The space complexity of insertion is O(M) as in the worst case
# we must create a new node for each char

# Time complexity of Search is O(M) in the worst case since we must check for the existence of each char in M.
# Space complexity of search is O(1)

# Time complexity of prefix search is O(M) for the same reasons as search
# space complexity is O(1)

# Trie node class. A Trie is a tree like structure consisting of trienodes 

class TrieNode:
    
    end = None
    
    def __init__(self):
        self.links = [None] * 26
        
    def containsKey(self,ch):
        return self.links[ord(ch) - ord('a')] != None
    
    def get(self,ch):
        return self.links[ord(ch) - ord('a')]
    
    def put(self,ch, node):
        self.links[ord(ch) - ord('a')] = node
        
    def setEnd(self):
        self.end = True
    
    def isEnd(self):
        return self.end
    