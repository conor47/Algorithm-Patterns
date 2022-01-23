# Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

# Recall that:

#     The node of a binary tree is a leaf if and only if it has no children
#     The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
#     The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def postOrder(node):
            if not node:
                return 0,None
            
            depth1,leftNode = postOrder(node.left)
            depth2,rightNode = postOrder(node.right)
            
            if depth1 == depth2:
                return depth1 + 1,node
            
            elif depth1 > depth2:
                return depth1 + 1,leftNode
            else:
                return depth2 + 1,rightNode
        
        depth,node = postOrder(root)
        return node

# Time complexity is O(N)

# Space complexity is O(N)