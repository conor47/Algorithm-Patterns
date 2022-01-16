# Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

# Note that you need to maximize the answer before taking the mod and not after taking it.

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        sums = []
        
        def dfs(node):
            if not node:
                return 0
            
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            sums.append(leftSum + rightSum + node.val)
            return leftSum + rightSum + node.val
       
        total = dfs(root)
        res = 0
        for i in range(len(sums)):
            res = max(res,sums[i] *(total - sums[i]))
        
        return res % (10**9 + 7)

# Time complexity is O(N)

# Space complexity is O(N)