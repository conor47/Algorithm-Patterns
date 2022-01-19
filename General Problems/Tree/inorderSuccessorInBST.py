# Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

# The successor of a node p is the node with the smallest key greater than p.val.

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        
        values = []
         
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
        
        def dfs(node,val):
            if not node:
                return None
            if node.val == val:
                return node
            return dfs(node.left,val) or dfs(node.right,val)
            
            
        inorder(root)     
        
        target = float('inf')
        for idx,num in enumerate(values):
            if num == p.val:
                if idx == len(values) -1:
                    return None
                target = values[idx+1]
                break
       
        if target == float('inf'):
            return None
        
        return dfs(root,target) 

# Time complexity is O(N)

# Space complexity is O(N)

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        
        successor = None
        
        while root:
            
            if p.val >= root.val:
                root = root.right
            
            else:
                successor = root
                root = root.left
            
        return successor

# Space complexity O(1)