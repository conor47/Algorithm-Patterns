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
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        
        root = node
        while root.parent:
            root = root.parent
        
        successor = None
        
        while root:
            
            if node.val >= root.val:
                root = root.right
            
            else:
                successor = root
                root = root.left
        
        return successor

# Time complexity is O(N)

# Space complexity is O(N)