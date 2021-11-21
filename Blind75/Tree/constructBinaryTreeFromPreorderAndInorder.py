# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val:idx for idx,val in enumerate(inorder)}
        
        def helper(left,right):
            if left > right:
                return None
            
            val = preorder.pop(0)
            node = TreeNode(val)
            index = idx_map[val]
            
            node.left = helper(left,index-1)
            node.right = helper(index+1, right)
            
            return node
        
        return helper(0,len(inorder) -1)

# Time complexity is O(N)

# Space complexity is O(N) for the hash map and for the system call stack used in recursion. On average the call stack
# takes O(Log N) space and in the worst case it takes O(N) space