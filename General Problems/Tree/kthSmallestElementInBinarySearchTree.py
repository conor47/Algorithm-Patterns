# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.inorder(root,res)
        return res[k-1]
    
    def inorder(self,node,res):
        if not node:
            return
        self.inorder(node.left,res)
        res.append(node.val)
        self.inorder(node.right,res)
    
# Time complexity is O(N)

# Space complexity is O(N)