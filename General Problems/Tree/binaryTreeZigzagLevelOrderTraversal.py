# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

import collections

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = collections.deque()
        queue.append(root)
        zig = False
        while queue:
            length = len(queue)
            levelOrder = []
            for i in range (length):
                node = queue.popleft()
                levelOrder.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if zig:
                res.append([* levelOrder[::-1]])
            else:
                res.append([* levelOrder])
            zig = not zig
        return res

# Time complexity is O(N)

# Space complexity is O(N). At most the size of the queue would be no more than 2 * L where L is the max number of nodes on a level
# Theoretically at most this would be all of the leaf nodes in a full binary tree which is ~ equivalent to N/2 , this the overall space
# complexity is O(2 * N/2) or O(N)