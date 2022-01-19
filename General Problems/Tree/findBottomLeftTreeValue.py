# Given a node in a binary search tree, return the in-order successor of that node in the BST. If that node has no in-order successor, return null.

# The successor of a node is the node with the smallest key greater than node.val.

# You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:

# class Node {
#     public int val;
#     public Node left;
#     public Node right;
#     public Node parent;
# }

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        def maxDepth(node):
            if not node:
                return 0
            left = maxDepth(node.left)
            right = maxDepth(node.right)
            
            return max(left,right) + 1
        
        def inorder(node,depth,target):
            if not node:
                return
            if depth == target:
                return node
            return inorder(node.left,depth+1,target) or inorder(node.right,depth+1,target)
        
        depth = maxDepth(root)
        
        res = inorder(root,1,depth)
        return res.val if res else None

# Time complexity is O(N)

# Space complexity is O(N)