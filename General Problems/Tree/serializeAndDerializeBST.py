# Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

# The encoded string should be as compact as possible.

 

# Example 1:

# Input: root = [2,1,3]
# Output: [2,1,3]

# Example 2:

# Input: root = []
# Output: []

import collections

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def preorder(node):
            if node is None:
                return 'x'
            
            s = str(node.val) + ',' + preorder(node.left) + ',' + preorder(node.right)
            return s 
    
        return preorder(root)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        queue = collections.deque()
        nodes = data.split(',')
        
        for i in  nodes:
            queue.append(i)
            
        def helper(queue):
            if not queue:
                return None
            
            val= queue.popleft()
            if val is 'x':
                return None
                
            node = TreeNode(int(val))
            node.left = helper(queue)
            node.right = helper(queue)
            return node
        
        return helper(queue)

# Time complexity is O(N)

# Space complexity is O(N)