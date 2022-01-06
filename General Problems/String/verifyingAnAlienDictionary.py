# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

 

# Constraints:

#     1 <= words.length <= 100
#     1 <= words[i].length <= 20
#     order.length == 26
#     All characters in words[i] and order are English lowercase letters.

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i in range(len(order)):
            dic[order[i]] = i
        
        def check(s1,s2):
            m = min(len(s1),len(s2))
            for i in range(m):
                if dic[s1[i]] > dic[s2[i]]:
                    return False
                elif dic[s1[i]] < dic[s2[i]]:
                    return True
            return len(s1) <= len(s2)
        
        for i in range(len(words)-1):
            if dic[words[i][0]] < dic[words[i+1][0]]:
                continue
            elif dic[words[i][0]] > dic[words[i+1][0]]:
                return False
            else:
                if not check(words[i],words[i+1]):
                    return False
        return True

