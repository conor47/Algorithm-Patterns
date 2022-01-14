# Given the root of a binary tree, return the maximum width of the given tree.

# The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes are also counted into the length calculation.

# It is guaranteed that the answer will in the range of 32-bit signed integer.

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        q = deque()
        q.append((root,0))
        
        while q:
            _,level = q[0]
            
            for _ in range(len(q)):
                node,idx = q.popleft()
                
                if node.left:
                    q.append((node.left,idx * 2))
                if node.right:
                    q.append((node.right,idx*2+1))
            res = max(res,idx - level + 1)
        return res

# Time complexity is O(N)

# Space complexity is O(N) since the queue will hold at most 2 levels of the tree at one time. In a complete binary tree the bottom level can contain
# up to n/2 nodes.