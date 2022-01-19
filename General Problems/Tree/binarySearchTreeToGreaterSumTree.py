# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

# As a reminder, a binary search tree is a tree that satisfies these constraints:

#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.


class Solution:
    s = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def treeSum(node):
            if not node:
                return 0
            left = treeSum(node.left)
            right = treeSum(node.right)
            return node.val + left + right
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            temp = node.val 
            node.val = self.s
            self.s -= temp
            inorder(node.right)
            
        self.s = treeSum(root)
        inorder(root)
        return root

# Time complexity is O(N)

# Space complexity is O(N)