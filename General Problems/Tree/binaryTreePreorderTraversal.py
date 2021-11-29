# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Input: root = [1,null,2,3]
# Output: [1,2,3]

# recursive solution

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        return res

# Time complexity is O(N)

# Space complexity is O(N) as in the worst case the tree is a linked list

# Iterative solution

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        
        if not root:
            return res
        stack.append(root)
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

# Time complexity is O(N)

# Space complexity is O(N)