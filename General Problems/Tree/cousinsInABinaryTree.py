# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

# Two nodes of a binary tree are cousins if they have the same depth with different parents.

# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
         
        if not root:
            return False
        
        def dfs(node,target,level,parent):
            if not node:
                return None
            if node.val == target:
                return (parent,level)
            return dfs(node.left,target,level+1,node) or dfs(node.right,target,level+1,node)
        
                
        parent, level = dfs(root,x,0,None)
        parent2,level2 = dfs(root,y,0,None)

        return parent != parent2 and level == level2

# Time complexity is O(N) 

# Space complexity is O(N)