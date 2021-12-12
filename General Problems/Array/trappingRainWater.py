# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        
        lMax = 0
        for i in range(len(height)):
            leftMax[i] = lMax
            lMax = max(lMax,height[i])
        
        rMax = 0
        for i in range(len(height)-1,-1,-1):
            rightMax[i] = rMax
            rMax = max(rMax,height[i])
        
        lrMin = [0] * len(height)
        for i in range(len(height)):
            lrMin[i] = min(leftMax[i],rightMax[i])
            
        res = 0
        for i in range(len(height)):
            h = lrMin[i] - height[i]
            if h > 0:
                res += h
        return res

# Time complexity is O(N)

# Space complexity is O(N)