# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [0] * n
        right = [0] * n
        
        rstack = []
        lstack = []
        
        for i in range(n-1,-1,-1):
            while rstack and heights[i] <= heights[rstack[-1]]:
                rstack.pop()
            if rstack:
                right[i] = rstack[-1] 
            else:
                right[i] = n
            rstack.append(i)
        
        
        for i in range(n):
            while lstack and heights[i] <= heights[lstack[-1]]:
                lstack.pop()
            if lstack:
                left[i] = lstack[-1]
            else:
                left[i] = -1 
            lstack.append(i) 
        res = float('-inf')
        
        for i in range(n):
            res = max(res,heights[i] * (right[i] - left[i] - 1)) 
        return res

# Time complexity is O(N)

# Space complexity is O(N)