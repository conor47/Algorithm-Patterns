# ou are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

# You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

# While moving from building i to building i+1 (0-indexed),

#     If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
#     If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.

# Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

# Based on the logic of always using ladders for the largest climbs we have seen so far. 

import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        n = len(heights)
        
        for i in range(n-1):
            if heights[i+1] <= heights[i]:
                i+=1
                continue
            elif ladders > 0:
                ladders -= 1
                heapq.heappush(heap,heights[i+1]-heights[i])
                i += 1
                continue
            elif len(heap) and heights[i+1] - heights[i] > heap[0] and bricks >= heap[0]:
                bricks -= heapq.heappop(heap)
                heapq.heappush(heap,heights[i+1] - heights[i])
                i += 1
                continue
            elif bricks >= heights[i+1] - heights[i]:
                bricks -= heights[i+1] - heights[i]
                i += 1
                continue
            else:
                break
        return i

# Time complexity is O(N Log L) where N is the length of the heights array and L the number of ladders. The heap will never be larger than
# L and so insertion and removal will take O(Log L) time

# Space complexity is O(L) for the heap

# Solution using the same logic but more simplified code

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        n = len(heights)
        
        for i in range(n-1):
            current = heights[i]
            nex = heights[i+1]
            diff = nex - current
            
            if diff <= 0:
                continue
            
            else:
                heapq.heappush(heap,diff)
                if len(heap) > ladders:
                    bricks -= heapq.heappop(heap)
                    if bricks < 0:
                        return i
        return n - 1