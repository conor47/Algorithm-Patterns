# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        count = 0
        
        if 'b' not in counts or 'a' not in counts or 'l' not in counts or 'o' not in counts or 'n' not in counts:
            return 0
        
        lcount = counts['l'] //2
        ocounts = counts['o'] //2
        
        return min(lcount,ocounts,counts['a'],counts['b'],counts['n'])

# Time complexity is O(N)

# Space complexity is O(N)