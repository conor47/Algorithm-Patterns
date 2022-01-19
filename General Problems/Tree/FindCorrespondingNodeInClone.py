# Given two binary trees original and cloned and given a reference to a node target in the original tree.

# The cloned tree is a copy of the original tree.

# Return a reference to the same node in the cloned tree.

# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(original,cloned,target):
            if not original:
                return 
            if original == target:
                return cloned
            return dfs(original.left,cloned.left,target) or dfs(original.right,cloned.right,target)
        
        return dfs(original,cloned,target)

# Time complexity is O(N)

# Space complexity is O(N)