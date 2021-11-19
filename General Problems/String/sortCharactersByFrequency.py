# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

 

# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.

# Example 3:

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

 

# Constraints:

#     1 <= s.length <= 5 * 105
#     s consists of uppercase and lowercase English letters and digits.

import collections
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        count = collections.Counter(s)
        maxHeap = []
        for key,value in count.items():
            heapq.heappush(maxHeap,(-value,key))
        result = ''
        while(len(maxHeap)):
            [count,char] = heapq.heappop(maxHeap)
            result += char * -count
        return result

# Time complexity is O(N). Each push and pop opearation in the heap takes O(Log K)
# time , where k is the number of distinct chars in the input string

# Space complexity is O(N). In the worst case every char is unique and our heap and 
# count object will store N items