# Given the root of a binary tree, collect a tree's nodes as if you were doing this:

#     Collect all the leaf nodes.
#     Remove all the leaf nodes.
#     Repeat until the tree is empty.

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        pairs = defaultdict(list)
        self.getHeight(root,pairs) 
        return pairs.values()
        
    def getHeight(self,node,pairs):
        if not node:
            return -1
        
        left = self.getHeight(node.left,pairs)
        right = self.getHeight(node.right,pairs)
        current = max(left,right) + 1
        pairs[current].append(node.val)
        return current

# Time complexity is O(N)

# Space complexity is O(N)

