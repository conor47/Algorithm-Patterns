# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        m = float('-inf')
        res = 0
        level = 1
        while q:
            l = len(q)
            s = 0
            for i in range(l):
                node = q.pop(0)
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if s > m:
                m = s
                res = level
            level += 1
        return res

# Time complexity is O(N)

# Space complexity is O(N)