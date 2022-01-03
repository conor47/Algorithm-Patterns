# A string s is called good if there are no two different characters in s that have the same frequency.

# Given a string s, return the minimum number of characters you need to delete to make s good.

# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

 

# Example 1:

# Input: s = "aab"
# Output: 0
# Explanation: s is already good.

# Example 2:

# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

# Example 3:

# Input: s = "ceabaacb"
# Output: 2
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

 

# Constraints:

#     1 <= s.length <= 105
#     s contains only lowercase English letters.



class Solution:
    def minDeletions(self, s: str) -> int:
        if len(s) == 1:
            return 0
        counts = Counter(s)
        res = 0
        freq = [0 for _ in range(len(s) + 1)]
        for num in counts.values():
            freq[num] += 1
        for i in range(len(freq) -1 ,0,-1):
            while freq[i] > 1:
                freq[i] -= 1
                freq[i-1] += 1
                res += 1 
        return res

# Time complexity is O(N)

# Space complexity is O(N)