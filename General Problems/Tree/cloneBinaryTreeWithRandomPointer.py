# A binary tree is given such that each node contains an additional random pointer which could point to any node in the tree or null.

# Return a deep copy of the tree.

# The tree is represented in the same input/output way as normal binary trees where each node is represented as a pair of [val, random_index] where:

#     val: an integer representing Node.val
#     random_index: the index of the node (in the input) where the random pointer points to, or null if it does not point to any node.

# You will be given the tree in class Node and you should return the cloned tree in class NodeCopy. NodeCopy class is just a clone of Node class with the same attributes and constructors.

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        
        clones = {}
        
        def clone(node):
            if not node:
                return None
            if node in clones:
                return clones[node]
            
            newNode = NodeCopy(node.val)
            clones[node] = newNode
            newNode.left = clone(node.left)
            newNode.right = clone(node.right)
            newNode.random = clone(node.random)
            return newNode
        
        return clone(root)

# Time complexity is O(N)

# Space complexity is O(N)