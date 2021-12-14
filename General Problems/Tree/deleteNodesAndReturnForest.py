# Given the root of a binary tree, each node in the tree has a distinct value.

# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

# Return the roots of the trees in the remaining forest. You may return the result in any order.

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        deleted = set(to_delete)
        res = []
        
        def helper(root,is_root):
            if not root:
                return None
            root_del = root.val in deleted
            if is_root and not root_del:
                res.append(root)
            
            root.left = helper(root.left,root_del)
            root.right = helper(root.right,root_del)
            return None if root_del else root
            
        helper(root,True)
        return res

# Time complexity is O(N) since we are visiting every node

# Space complexity is O(H + N) where H is the height of the tree