# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# recursive solution

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(node1,node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            return node1.val == node2.val and isMirror(node1.left,node2.right) and isMirror(node1.right,node2.left)
        
        return isMirror(root,root)

# Time complexity is O(N)

# Space complexity is O(N)

# iterative solution

import collections

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = collections.deque()
        queue.append(root)
        queue.append(root)
        while queue:
            n1 = queue.popleft()
            n2 = queue.popleft()
            if n1 is None and n2 is None:
                continue
            if n1 is None or n2 is None:
                return False
            if n1.val != n2.val:
                return False
            queue.append(n1.left)
            queue.append(n2.right)
            queue.append(n1.right)
            queue.append(n2.left)
        return True