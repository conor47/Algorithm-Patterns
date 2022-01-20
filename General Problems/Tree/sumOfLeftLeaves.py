# Given the root of a binary tree, return the sum of all left leaves.

class Solution:
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 0
        
        res = 0
        q = [root]
        
        while q:
            
            level_length = len(q)
            for i in range(level_length):
                
                node = q.pop(0)
                
                
                if node.left and not node.left.left and not node.left.right:
                    res += node.left.val
                    q.append(node.left)
                
                elif node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
        
        return res

# Time complexity is O(N)

# Space complexity is O(N)