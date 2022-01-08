# Given the root of a binary tree, the depth of each node is the shortest distance to the root.

# Return the smallest subtree such that it contains all the deepest nodes in the original tree.

# A node is called the deepest if it has the largest depth possible among any node in the entire tree.

# The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        nodes = set()
        
        def maxDepth(node):
            if not node:
                return 0
            return 1 + max(maxDepth(node.left),maxDepth(node.right))
        
        def paint(node,depth,m):
            if not node:
                return
            if depth == m:
                nodes.add(node)
                return
            paint(node.left,depth+1,m)
            paint(node.right,depth+1,m)
            
        m = maxDepth(root)
        paint(root,1,m)
        
        def find(node):
            if not node:
                return False
            if node in nodes:
                return node
            left = find(node.left)
            right = find(node.right)
            if left and right:
                return node
            else:
                return left or right
        return find(root)

# Time complexity is O(N)

# Space complexity is (N) for the recursin stack as in the worst case the tree may be a linked list