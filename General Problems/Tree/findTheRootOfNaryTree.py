# You are given all the nodes of an N-ary tree as an array of Node objects, where each node has a unique value.

# Return the root of the N-ary tree.

# Custom testing:

# An N-ary tree can be serialized as represented in its level order traversal where each group of children is separated by the null value (see examples).

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        
        seen = set()
        
        for node in tree:
            for child in node.children:
                seen.add(child.val)
            
        for node in tree:
            if node.val not in seen:
                return node

# Time complexity is O(N)

# Space complexity is O(N)