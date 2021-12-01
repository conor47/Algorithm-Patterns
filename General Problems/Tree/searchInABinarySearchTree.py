# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.val == val or root is None:
            return root
        
        return self.searchBST(root.left,val) or self.searchBST(root.right,val)

# Time complexity is O(H) where H is the height of the tree. Results in O(N) in the worst case and O(Log N) in the best case

# Space complexity is the same at O(H) or O(N) in the worst case and O(Log N) in the best case  