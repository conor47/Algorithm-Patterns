# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

# Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

# Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return (0,0)
            
            left = helper(node.left)
            right = helper(node.right)
            
            rob = node.val + left[1] + right[1]
            not_rob = max(left) + max(right)
            return[rob,not_rob]
        
        return max(helper(root))
        
# Time complexity is O(N) since we visit all nodes

# Space complexity is O(N) in the worst case and O(Log N) in the best case