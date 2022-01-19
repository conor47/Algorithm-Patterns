# Given the root of a binary tree, return the sum of values of its deepest leaves. 

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def depth(node):
            if not node:
                return 0
            
            left = depth(node.left)
            right = depth(node.right)
            return max(left,right) + 1
        
        def maxSum(node,depth,maxDepth):
            if not node:
                return 0
            if depth == maxDepth:
                return node.val
            left = maxSum(node.left,depth+1,maxDepth)
            right = maxSum(node.right,depth+1,maxDepth)
            return left + right
            
            
        
        maxDepth = depth(root)
        return maxSum(root,1,maxDepth)

# Time complexity is O(N) where N is the number of nodes in the tree

# Space complexity is O(N) for the recursion stack