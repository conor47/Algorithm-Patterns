# Given the root of a binary tree, return the maximum average value of a subtree of that tree. Answers within 10-5 of the actual answer will be accepted.

# A subtree of a tree is any node of that tree plus all its descendants.

# The average value of a tree is the sum of its values, divided by the number of nodes.

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.res = float('-inf') 
        
        def recurse(root,nodes,s):
            if not root:
                return (0,0)
            nodes_left,sum_left = recurse(root.left,0,0)
            nodes_right,sum_right = recurse(root.right,0,0)
            average = (root.val + sum_left + sum_right) / (nodes_left + nodes_right + 1)
            self.res = max(self.res,average) 
            return (nodes_left+nodes_right +1,root.val + sum_left + sum_right)
        recurse(root,0,0)
        return self.res

# Time complexity is O(N)

# Space complexity is O(N) in the worst case and O(Log N) in the average case