# Given a root of an N-ary tree, return a deep copy (clone) of the tree.

# Each node in the n-ary tree contains a val (int) and a list (List[Node]) of its children.

# class Node {
#     public int val;
#     public List<Node> children;
# }

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return root
        clones = {}
        
        def traverse(node):
            if not node:
                return
            clone = Node(node.val)
            clones[node] = clone
            
            for child in node.children:
                traverse(child)
                clone.children.append(clones[child])
        
        traverse(root)
        return clones[root]
    
# Time complexity is O(N)

# Space complexity is O(N)