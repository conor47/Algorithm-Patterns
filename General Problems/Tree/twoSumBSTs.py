# Given the roots of two binary search trees, root1 and root2, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        def search(val):
            
            node = root2
            while node:
                
                if node.val == val:
                    return True
                elif node.val > val:
                    node = node.left
                else:
                    node = node.right
            return False
        
        def dfs(node):
            if not node:
                return False
            if search(target - node.val):
                return True
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root1)

# Time complexity is O(N Log M)

# Space complexity is O(N)
