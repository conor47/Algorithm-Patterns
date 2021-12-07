# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

# A row i is weaker than a row j if one of the following is true:

#     The number of soldiers in row i is less than the number of soldiers in row j.
#     Both rows have the same number of soldiers and i < j.

# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

 

# Example 1:

# Input: mat = 
# [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]], 
# k = 3
# Output: [2,0,3]
# Explanation: 
# The number of soldiers in each row is: 
# - Row 0: 2 
# - Row 1: 4 
# - Row 2: 1 
# - Row 3: 2 
# - Row 4: 5 
# The rows ordered from weakest to strongest are [2,0,3,1,4].

# Example 2:

# Input: mat = 
# [[1,0,0,0],
#  [1,1,1,1],
#  [1,0,0,0],
#  [1,0,0,0]], 
# k = 2
# Output: [0,2]
# Explanation: 
# The number of soldiers in each row is: 
# - Row 0: 1 
# - Row 1: 4 
# - Row 2: 1 
# - Row 3: 1 
# The rows ordered from weakest to strongest are [0,2,3,1].

 

# Constraints:

#     m == mat.length
#     n == mat[i].length
#     2 <= n, m <= 100
#     1 <= k <= m
#     matrix[i][j] is either 0 or 1.

# First naieve solution

import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for index,row in enumerate(mat):
            count = 0
            for i in row:
                if i == 1:
                    count += 1
                else:
                    break
            heapq.heappush(heap,(-count,-index))
            if len(heap) > k:
                heapq.heappop(heap)
        

        res = []
        while heap:
            res.append(-heapq.heappop(heap)[1])
        return res[::-1]

# Time complexity is O(MN Log K)
# Space complexity is O(K)

# using binary search to find the strength of each row is a more efficient approach

import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for index,row in enumerate(mat):
            count = self.binarySearch(row)            
            heapq.heappush(heap,(-count,-index))
            if len(heap) > k:
                heapq.heappop(heap)
        

        res = []
        while heap:
            res.append(-heapq.heappop(heap)[1])
        return res[::-1]
    
    def binarySearch(self,row):
        left = 0
        right = len(row)
        while left < right:
            mid = left + (right - left) // 2
            if row[mid] == 1:
                left = mid + 1
            else:
                right = mid
        return left

# Time complexity of calculating the strengths is O(M Log N). Inserting items and into the heap is done in O(Log K) time and we have a max possible
# m insertions making the time complexity O(M Log K). We can not say which is bigger this the total time complexity will be 
# m * (Log n + log k) which is O(M Log nk)

# Space complexity is O(k)