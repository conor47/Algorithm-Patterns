# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

#     WordDictionary() Initializes the object.
#     void addWord(word) Adds word to the data structure, it can be matched later.
#     bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

 

# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True

 

# Constraints:

#     1 <= word.length <= 500
#     word in addWord consists lower-case English letters.
#     word in search consist of  '.' or lower-case English letters.
#     At most 50000 calls will be made to addWord and search.

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        root = self.root
        for char in word:
            root = root.children.setdefault(char,TrieNode())
        root.isEnd = True
                

    def search(self, word: str) -> bool:
        
        def dfs(node,index):
            if index == len(word):
                return node.isEnd
            
            if word[index] == '.':
                for child in node.children:
                    if dfs(node.children[child], index+1):
                        return True
                    
            elif word[index] in node.children:
                return dfs(node.children[word[index]], index+1)
            
            return False
        
        return dfs(self.root,0)

# Space complexity is O(M) where M is the length of all the words in our Trie. in practice it will be lower than M due to many words 
# sharing a common prefix

# Time complexity is O(M) for search. In the worst case where we have a string like .... we can visit all nodes in the tree. For strings
# without any . the time complexity is O(H) where H is the length of the word 
class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False
