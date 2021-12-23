# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = [root]
        while q:
            rowLen = len(q)
            m = float('-inf')
            for i in range(rowLen):
                node = q.pop(0)
                m = max(m,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(m)
        return res

# Time complexity is O(N) 

# Space complexity is O(N)