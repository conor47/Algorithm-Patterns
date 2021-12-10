# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

 

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

# Example 3:

# Input: s = "a##c", t = "#a#c"
# Output: true
# Explanation: Both s and t become "c".

# Example 4:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

 

# Constraints:

#     1 <= s.length, t.length <= 200
#     s and t only contain lowercase letters and '#' characters.

# Stack solution

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.build(s) == self.build(t)
    
    def build(self,s):
        ans = []
        for char in s:
            if char != '#':
                ans.append(char)
            elif ans:
                ans.pop()
        return ''.join(ans)

# Time complexity is O(N + M)

# Space complexity O(N + M)

# Two pointers solution

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return all(x==y for x,y in itertools.zip_longest(self.helper(s),self.helper(t)))
    
    def helper(self,s):
        skip = 0
        for char in reversed(s):
            if char == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield char