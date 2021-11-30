# First the given nodes p and q are to be searched in a binary tree and then their lowest common ancestor is to be found. We can resort to a normal tree traversal to search for the two nodes. Once we reach the desired nodes p and q, we can backtrack and find the lowest common ancestor.

class Solution:
    ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def recursive(node):
            
            if not node:
                return False
            
            left = recursive(node.left)
            
            right = recursive(node.right)
            
            mid = node == p or node == q
            
            if mid + left + right >= 2:
                self.ans = node
                
            return mid or left or right
        
        recursive(root)
        return self.ans

# Time solution is O(N)

# Space complexity is O(N)

# Iterative approach

class Solution:
    ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        stack = [root]
        
        parent = {root:None}
        
        while p not in parent or q not in parent:
            node = stack.pop()
            
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        ancestors = set()
        
        while p:
            ancestors.add(p)
            p = parent[p]
        
        while q not in ancestors:
            q = parent[q]
        return q

# Time complexity is O(N)

# Space complexity is O(N)