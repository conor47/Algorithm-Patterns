# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once).

# Return the sum of lengths of all good strings in words.

 

# Example 1:

# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

# Example 2:

# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

 

# Constraints:

#     1 <= words.length <= 1000
#     1 <= words[i].length, chars.length <= 100
#     words[i] and chars consist of lowercase English letters.

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        res = 0 
        chars = Counter(chars)
        
        for word in words:
            if len(word) > len(chars):
                continue
            word_chars = Counter(word)
            chars.subtract(word_chars)
            for char in chars:
                if chars[char] < 0:
                    break
            else:
                res += len(word)
            chars.update(word_chars) 
        
        return res

# Time complexity is O(N * M) where N is the number of words and M is the length of the characters string

# Space complexity is O(1)