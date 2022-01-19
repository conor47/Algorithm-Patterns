# In an infinite binary tree where every node has two children, the nodes are labelled in row order.

# In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        
        res = []
        node_count = 1
        level = 1
        
        while label >= node_count*2:
            node_count *= 2
            level += 1
        
        while label != 0:
            res.append(label)
            level_max = (2**level) - 1
            level_min = 2**(level-1)
            label = int((level_max + level_min - label) /2)
            level -= 1
        
        return res[::-1]

# Time complexity is O(Log N)

# Space complexity is O(1)