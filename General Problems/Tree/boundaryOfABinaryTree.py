# The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

# The left boundary is the set of nodes defined by the following:

#     The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
#     If a node in the left boundary and has a left child, then the left child is in the left boundary.
#     If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
#     The leftmost leaf is not in the left boundary.

# The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

# The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

# Given the root of a binary tree, return the values of its boundary.

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root.left and not root.right:
            return [root.val]
        res = [root.val]
        self.leftBoundary(root.left,res)
        self.leaves(root,res)
        self.rightBoundary(root.right,res)
        return res

    
    def leftBoundary(self, node, res):
        if not node:
            return
        
        
        if not node.left and not node.right:
            return
        
        res.append(node.val)
        
        if node.left:
            self.leftBoundary(node.left,res)
            return
        elif node.right:
            self.leftBoundary(node.right,res)
    
    def rightBoundary(self, node, res):
        if not node:
            return
        
        if not node.left and not node.right:
            return
        
        if node.right:
            self.rightBoundary(node.right,res)
        elif node.left:
            self.rightBoundary(node.left,res)
        res.append(node.val)
            
    def leaves(self,node,res):
        if not node:
            return
        
        if not node.left and not node.right:
            res.append(node.val)
        
        self.leaves(node.left,res)
        self.leaves(node.right,res)

# Time complexity is O(N)

# Space complexity is O(N)