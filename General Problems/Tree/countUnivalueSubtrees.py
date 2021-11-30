# Given the root of a binary tree, return the number of uni-value subtrees.

# A uni-value subtree means all nodes of the subtree have the same value.

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.count = 0
        self.is_uni(root)
        return self.count
    
    def is_uni(self,node):
        
        if node.left is None and node.right is None:
            self.count+=1
            return True
        
        is_uni = True
        
        if node.left is not None:
            is_uni = self.is_uni(node.left) and is_uni and node.left.val == node.val
        if node.right is not None:
            is_uni = self.is_uni(node.right) and is_uni and node.right.val == node.val
        
        self.count += is_uni
        return is_uni

# Time complexity is O(N)

# Space complexity is O(H). The call stack is bound by the height of the tree

