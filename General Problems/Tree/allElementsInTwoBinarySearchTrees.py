# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        res = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
            
        inorder(root1)
        inorder(root2)
        return sorted(res)

# Time complexity is O(M + N)

# Space complexity is O(N + M)