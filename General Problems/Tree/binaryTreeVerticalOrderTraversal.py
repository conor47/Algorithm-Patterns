# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        traversal = defaultdict(list)
        self.bfs(root,0,0,traversal)
        print(traversal)
        res = []
        for col, nodes in sorted(traversal.items()):
            res.append(nodes)
        return res
        
    def bfs(self,node,col,row,traversal):
        if not node:
            return
        queue = [(node,col,row)]
        while queue:
            node,col,row = queue.pop(0)
            traversal[col].append(node.val)
            if node.left:
                queue.append((node.left,col-1,row+1))
            if node.right:
                queue.append((node.right,col+1,row+1))

# time complexity is O(N LogN). The most costly operation in the algorithm is sorting the traversal map. Performing the breadth first search
# is O(N)

# Space complexity is O(N). 