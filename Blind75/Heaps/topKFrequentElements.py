# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

 

# Constraints:

#     1 <= nums.length <= 105
#     k is in the range [1, the number of unique elements in the array].
#     It is guaranteed that the answer is unique.

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        
        heap = []
        for num,count in counts.items():
            heapq.heappush(heap,(-count,num))
        
        while(len(heap) > 0 and k > 0):
            [count,num] = heapq.heappop(heap)
            res.append(num)
            k -= 1
        return res

# Time complexity O(N LogK) generating the counts dict takes O(N) time and the 
# heap operations take (LogK) time since we are storing at most K items in the heap

# Space complexity O(N + K)