# Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

# A grandparent of a node is the parent of its parent if it exists.

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def dfs(node,parent,grandparent):
            if not node:
                return 0
           
            left = dfs(node.left,node,parent)
            right = dfs(node.right,node,parent)
            
            if grandparent and grandparent.val % 2 == 0:
                return left + right + node.val
            else:
                return left + right
           
        return dfs(root,None,None)

# Time complexity is O(N)

# Space complexity is O(N)