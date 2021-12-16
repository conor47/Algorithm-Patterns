# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0 or len(t) > len(s):
            return ''
        
        counts = Counter(t)
        left,right = 0,0
        need = len(t)
        res = ''
        minLen = float('inf')
        
        while right < len(s):
            char = s[right]
            if char in counts:
                if counts[char] > 0:
                    need -= 1
                counts[char] = counts[char] - 1
                
            while need == 0:
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    res = s[left:right + 1]
                char = s[left]
                if char in counts:
                    counts[char] = counts[char] + 1
                    if counts[char] > 0:
                        need += 1
                left += 1
            right += 1
        return res
    
# Time complexity is O(S + T)

# Space complexity is O(T)