# You are given a list of equivalent string pairs synonyms where synonyms[i] = [si, ti] indicates that si and ti are equivalent strings. You are also given a sentence text.

# Return all possible synonymous sentences sorted lexicographically.

 

# Example 1:

# Input: synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], text = "I am happy today but was sad yesterday"
# Output: ["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]

# Example 2:

# Input: synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am happy today but was sad yesterday"
# Output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]

 

# Constraints:

#     0 <= synonyms.length <= 10
#     synonyms[i].length == 2
#     1 <= si.length, ti.length <= 10
#     si != ti
#     text consists of at most 10 words.
#     The words of text are separated by single spaces.

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        graph = defaultdict(list)
        bfs = collections.deque()
        for a,b in synonyms:
            graph[a].append(b)
            graph[b].append(a)
        ans = set()
        bfs.append(text)
        
        while bfs:
            sentence = bfs.popleft()
            ans.add(sentence)
            words = sentence.split()
            for i,w in enumerate(words):
                if w in graph:
                    for new_word in graph[w]:
                        new_sentence = ' '.join(words[:i] + [new_word] + words[i+1:])
                        if new_sentence not in ans:
                            bfs.append(new_sentence)
        return sorted(list(ans))
