# Given the root of a binary tree, find the largest subtree, which is also a Binary Search Tree (BST), where the largest means subtree has the largest number of nodes.

# A Binary Search Tree (BST) is a tree in which all the nodes follow the below-mentioned properties:

#     The left subtree values are less than the value of their parent (root) node's value.
#     The right subtree values are greater than the value of their parent (root) node's value.

# Note: A subtree must include all of its descendants.

class Solution:
    res = 0
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        def isBst(node,low,high):
            
            if not node:
                return True
            
            if high and node.val >= high or low and node.val <= low:
                return False
            
            return isBst(node.left,low,node.val) and isBst(node.right,node.val,high)
        
        def nodeCount(node):
            if not node:
                return 0
            
            left = nodeCount(node.left)
            right = nodeCount(node.right)
            return left + right + 1
        
        def recurse(node):
            if not node:
                return
            if isBst(node,None,None):
                self.res = max(self.res,nodeCount(node))
            
            recurse(node.left)
            recurse(node.right)
            
            
        recurse(root)
        return self.res

# Time complexity is O(N^2)

# Space complexity is O(N)