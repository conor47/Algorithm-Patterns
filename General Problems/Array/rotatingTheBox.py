# You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

#     A stone '#'
#     A stationary obstacle '*'
#     Empty '.'

# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

# It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

# Return an n x m matrix representing the box after the rotation described above.

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            for i in range(len(row)-1,-1,-1):
                if row[i] == '#':
                    self.move(row,i)
        newBox = []
        for m in range(len(box[0])):
            level = []
            for n in range(len(box)-1,-1,-1):
                level.append(box[n][m])
            newBox.append(level)
        return newBox
                
    
    def move(self,row,idx):
        if idx < len(row) - 1:
            while idx < len(row) -1 and row[idx+1] == '.':
                row[idx] = '.'
                row[idx + 1] = '#'
                idx +=1 

# Time complexity is O(MN^2 * M * N)

# Space complexity is O(MN) if we consider the newBox grid

# Same logic, more succint code

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for i in range(len(nums)):
            prefix = 0
            for j in range(i,len(nums)):
                prefix += nums[j]
                sums.append(prefix)
        sums.sort()
        return sum(sums[left-1:right])%(10**9+7)

        