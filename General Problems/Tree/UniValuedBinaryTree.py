# A binary tree is uni-valued if every node in the tree has the same value.

# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        
        def recurse(node,val):
            if not node:
                return True
            if node.val != val:
                return False
            return recurse(node.left,val) and recurse(node.right,val)
        
        return recurse(root,val)

# Time complexity is O(N)

# Space complexity is O(N)