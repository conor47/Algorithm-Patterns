# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        minDepth = [float('inf')]
        
        def recursive(node,depth,minD):
            if node is None:
                return
            if not node.left and not node.right:
                minD[0] = min(minD[0],depth)
                return
            recursive(node.left,depth+1,minD)
            recursive(node.right,depth+1,minD)
        recursive(root,1,minDepth)
        return minDepth[0]

# Time complexity is O(N)

# Space complexity is O(N)

# Performing an iterative BFS when we hit a leaf node its guaranteed to be the min depth

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque()
        queue.append((root,1))
        
        while queue:
            node,level  = queue.popleft()
            if not node.left and not node.right:
                return level
            
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
        return 0

# Time complexity is O(N/2) or O(N). In the worst case the binary tree is balanced and we must visit every node execept those in last level.

# space complexity is O(N)