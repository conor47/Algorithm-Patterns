# For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

# A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

# Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return not root1 and not root2
        
        if root1.val != root2.val:
            return False
        
        return self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right) or self.flipEquiv(root1.left,root2.right) and self.flipEquiv(root1.right,root2.left)

# Time complexity is O(min(M,N))

# Space complexity is O(min(N,M))