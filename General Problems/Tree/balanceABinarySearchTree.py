# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

# first solution using helper methods

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        values = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
        
        def balanced(vals):
            if len(vals) == 0:
                return None
            mid = len(vals) // 2
            node = TreeNode(vals[mid])
            node.left = balanced(vals[:mid])
            node.right = balanced(vals[mid+1:])
            return node
            
        inorder(root)
        return balanced(values)

# Time complexity is O(N)

# Space complexity is O(N) for the recursion stack and since we are storing every nodes values 