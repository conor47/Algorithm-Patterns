# Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.

# Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant (where we allow a node to be a descendant of itself) for every valid i". A descendant of a node x is a node y that is on the path from node x to some leaf node.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if root is None:
            return None
        
        if len(nodes) == 1:
            return nodes[0]
        
        parent = {root:None}
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
                
            
        while len(nodes) > 1:
            ancestors = []
            p = nodes.pop()
            while p:
                ancestors.append(p)
                p = parent[p]
            q = nodes.pop()
            while q not in ancestors:
                q = parent[q]
            nodes.append(q)
        return q

# Time complexity is O(N)

# Space complexity is O(N)