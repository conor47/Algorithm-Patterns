# Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

# If there exist multiple answers, you can return any of them.

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        node = TreeNode(postorder.pop())
        if len(preorder) == 1:
            return node
        rightIndex = preorder.index(postorder[-1])
        node.right = self.constructFromPrePost(preorder[rightIndex:], postorder)
        node.left = self.constructFromPrePost(preorder[1:rightIndex], postorder)
        
        return node

# time complexity is O(N)

# space complexity is O(H) or O(N) in the worst case