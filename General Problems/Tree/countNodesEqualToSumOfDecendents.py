# Given the root of a binary tree, return the number of nodes where the value of the node is equal to the sum of the values of its descendants.

# A descendant of a node x is any node that is on the path from node x to some leaf node. The sum is considered to be 0 if the node has no descendants.

class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        
        def recurse(node,count):
            if not node:
                return (0,0)
            
            left = recurse(node.left,count)
            right = recurse(node.right,count)
            count += left[1]
            count += right[1]
            s = left[0] + right[0]
            
            if node.val == s:
                count += 1
            return (node.val + s,count)
        
        s,res = recurse(root,0)
        return res

# Time complexity is O(N)

# Space complexity is O(N)