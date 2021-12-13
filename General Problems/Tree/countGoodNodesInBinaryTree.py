# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.isGood(root,float('-inf'))
    
    def isGood(self,node,m):
        if node is None:
            return 0
        
        left = self.isGood(node.left,max(m,node.val))
        right = self.isGood(node.right, max(m,node.val))
        
        if node.val >= m:
            return 1 + left + right
        else:
            return left + right

# Time complexity is O(N)

# Space complexity is O(1)

