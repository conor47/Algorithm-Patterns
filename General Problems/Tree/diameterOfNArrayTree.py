# The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

# (Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        maxDiameter = 0
        
        def diameter(node):
            nonlocal maxDiameter
            if not node:
                return 0
            max1 = 0
            max2 = 0
            for child in node.children:
                d = diameter(child)
                if d > max1:
                    max2 = max1
                    max1 = d
                    
                elif d > max2:
                    max2 = d
                maxDiameter = max(maxDiameter,max1+max2)
            return max(max1,max2) + 1
        
        diameter(root)
        return maxDiameter

# Time complexity is O(N) where N is the number of nodes in the tree

# Space complexity (N)