# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        
        def recursive(node,h,l):
            if not node:
                return
            nonlocal res
            res = max(res,abs(h - node.val), abs(l - node.val))
            h = max(h,node.val)
            l = min(l,node.val)
            recursive(node.left,h,l)
            recursive(node.right,h,l)
        recursive(root,root.val,root.val) 
        return res

# Time complexity is O(N) since we are visiting every node in the tree

# Space compexity is O(N) as in the worst case the tree is a linked list. Space complexity is O(Log N) in the best case