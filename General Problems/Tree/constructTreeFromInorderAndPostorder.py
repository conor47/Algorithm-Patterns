# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

#  Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]

# Example 2:

# Input: inorder = [-1], postorder = [-1]
# Output: [-1]

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_map = {val:idx for idx,val in enumerate(inorder)}
        
        def helper(left_idx, right_idx):
            if left_idx > right_idx:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)
            
            index = index_map[val]
            
            root.right = helper(index+1, right_idx)
            root.left = helper(left_idx, index - 1)
            
            return root
        
        return helper(0,len(inorder) - 1)

# Time complexity is O(N)

# Space complexity is O(N) for the hash map