# We can shift a string by shifting each of its letters to its successive letter.

#     For example, "abc" can be shifted to be "bcd".

# We can keep shifting the string to form a sequence.

#     For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".

# Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 

# Example 1:

# Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
# Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

# Example 2:

# Input: strings = ["a"]
# Output: [["a"]]

import collections

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        counts = collections.defaultdict(list)
                
        for s in strings:
            key = ()
            for i in range(len(s)-1):
                diff = ord(s[i+1]) - ord(s[i])
                key += (diff % 26,)
            counts[key].append(s)
        return counts.values()

# Time complexity is O(M) where M is the length of all the strings combined

# Space complexity is (M)