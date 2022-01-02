# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

# Example 1:

# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.

# Example 2:

# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"

# Example 3:

# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        i = 0
        count = 1
        while i < len(s) and  k <= len(s):
            if i > 0 and s[i] == s[i-1]:
                count += 1
                if count == k:
                    s = s[:i-k+1] + s[i+1:]
                    temp = k 
                    i -= k
                    while i > 0 and temp >0:
                        i -= 1
                        temp -= 1
                    continue
                else:
                    i += 1
            else:
                count = 1
                i += 1
            
        return s

# Time complexity is O(N)

# Space complexity is O(1)