# Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

# Implement the WordDistance class:

#     WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
#     int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.words = wordsDict
        self.pos = defaultdict(list)
        for index,word in enumerate(wordsDict):
            self.pos[word].append(index)

    def shortest(self, word1: str, word2: str) -> int:
        m = float('inf')
        for idx1 in self.pos[word1]:
            for idx2 in self.pos[word2]:
                m = min(m,abs(idx1 - idx2))
        return m    

# Time complexity of initialization is O(N). Time complexity of shortest operation is O(n^2)

# Space complexity is O(N)