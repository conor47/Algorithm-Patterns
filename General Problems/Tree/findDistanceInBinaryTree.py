# Given the root of a binary tree and two integers p and q, return the distance between the nodes of value p and value q in the tree.

# The distance between two nodes is the number of edges on the path from one to the other.

class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:

        def lca(node,p,q):
            if not node:
                return None
            if node.val == p or node.val == q:
                return node
            
            left = lca(node.left,p,q)
            right = lca(node.right,p,q)
            
            if right and left:
                return node
            elif left:
                return left
            elif right:
                return right
            else:
                return None
        def distance(node,target,dist):
            if not node:
                return
            if node.val == target:
                return dist
            return distance(node.left,target,dist+1) or distance(node.right,target,dist+1)
            
        lowest = lca(root,p,q)
        dist1 = distance(lowest,p,0)
        dist2 = distance(lowest,q,0)
        return dist1 + dist2

# Time complexity is O(N)

# Space complexity is O(N)