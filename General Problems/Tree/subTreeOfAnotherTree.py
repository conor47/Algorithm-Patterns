# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.]

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return not subRoot
        return self.isEqual(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
   
    def isEqual(self,root1,root2):
        if not root1 or not root2:
            return not root1 and not root2
        if root1.val != root2.val:
            return False
        return self.isEqual(root1.left,root2.left) and self.isEqual(root1.right,root2.right)

# Time complexity is O(N * M) where N and M are the number of nodes in the tree and subtree 

# Space complexity is O(M)