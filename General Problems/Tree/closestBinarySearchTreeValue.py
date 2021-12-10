# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root is None:
            return None
        closest = self.dfs(root,None,float('inf'),target)
        return closest.val
    
    
    def dfs(self,node,closestNode,dist,target):
        if node is None:
            return closestNode

        if node.val == target:
            closestNode = node
            return closestNode

        if(abs(node.val - target)) < dist:
            closestNode = node
            dist = abs(node.val - target)

        if node.val > target:
            return self.dfs(node.left,closestNode,dist,target)
            
        else:
            return self.dfs(node.right,closestNode,dist,target)

# Time complexity is O(Log N) or O(H) where H is the height of the tree

# Space complexity is O(H)

# Much simpler iterative binary search

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        while root:
            closest = min(closest,root.val, key = lambda x:abs(target-x))
            root = root.left if target < root.val else root.right
        return closest

# Time complexity is O(H)

# Space complexity O(1)