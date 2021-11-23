# Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.

# Example 1:

# Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
# Output: [4, 7]
# Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3.

# Example 2:

# Input: L1=[1, 9], L2=[4, 12], L3=[7, 10, 16]
# Output: [9, 12]
# Explanation: The range [9, 12] includes 9 from L1, 12 from L2 and 10 from L3.

import heapq
import math

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        rangeStart,rangeEnd = 0, math.inf
        currentMax = -math.inf
        minHeap = []
        
        for list in nums:
            heapq.heappush(minHeap,(list[0],0,list))
            currentMax = max(list[0], currentMax)
        
        while(len(minHeap) == len(nums)):
            val,index,arr = heapq.heappop(minHeap)
            if ((rangeEnd - rangeStart) > (currentMax - val)):
                rangeEnd = currentMax
                rangeStart = val
            
            if(index+1 < len(arr)):
                heapq.heappush(minHeap,(arr[index+1],index+1,arr))
                currentMax = max(currentMax, arr[index+1])
        
        return [rangeStart,rangeEnd]
        
# Time complexity is O(N Log M) since at most we will iteratea through each element once and we will store at max M elements on the heap
# heap operations will therefore be Log M in the worst case

# Space complexity is O(M) for the min heap