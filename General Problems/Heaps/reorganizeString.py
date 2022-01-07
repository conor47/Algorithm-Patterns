# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

 

# Example 1:

# Input: s = "aab"
# Output: "aba"

# Example 2:

# Input: s = "aaab"
# Output: ""

 

# Constraints:

#     1 <= s.length <= 500
#     s consists of lowercase English letters.

class Solution:
    def reorganizeString(self, s: str) -> str:
        
        chars = Counter(s) 
        res = '!'
        heap = [(-cnt,c) for c,cnt in chars.items()]
        heapq.heapify(heap)
        while heap:
            count,char = heapq.heappop(heap) 
            if char == res[-1]:
                if not heap:
                    return ''
                count2,char2 = heapq.heappop(heap)
                res += char2
                count2 += 1
                if count2 < 0:
                    heapq.heappush(heap,(count2,char2))
                heapq.heappush(heap,(count,char))
            else:
                res += char
                count += 1
                if count < 0:
                    heapq.heappush(heap,(count,char))
        return res[1:]

# Time complexity is O(N Log N)

# Space complexity is O(N)