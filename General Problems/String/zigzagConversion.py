# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"

 

# Constraints:

#     1 <= s.length <= 1000
#     s consists of English letters (lower-case and upper-case), ',' and '.'.
#     1 <= numRows <= 1000

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = [[] for _ in range(numRows) ]
        dir = 1
        idx = -1
        for i in range(len(s)):
            idx += dir
            if idx == 0:
                dir = 1
            elif idx == numRows-1:
                dir = -1
            arr[idx].append(s[i])
        res = ''
        for i in arr:
            for j in i:
                res += j
        return res

# Time complexity is O(N) where N is the length of the string

# Space complexity is O(N)