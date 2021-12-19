# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

#     a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check(root) != -1
    def check(self, node):
        if not node:
            return 0
        
        left = self.check(node.left)
        right = self.check(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1

# Time complexity is O(n)

# Space complexity is O(N) as in the worst case the tree may be a linked list©