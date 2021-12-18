# Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

# Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        return self.traverse(root,low,high)
    
    def traverse(self,node,low,high):
        if not node:
            return None
        if node.val < low:
            return self.traverse(node.right,low, high)
        elif node.val > high:
            return self.traverse(node.left, low, high)
        else:
            node.left = self.traverse(node.left, low, high)
            node.right = self.traverse(node.right, low, high)
            return node

# Time complexity is O(N)

# Space complexity is O(H) or O(N) in the worst case