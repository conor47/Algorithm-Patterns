# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []
        if not root:
            return res
        self.inorder(root,res)
        for i in range(0,len(res)-1):
            res[i].left = None
            res[i].right = res[i+1]
        res[-1].right, res[-1].left = None,None
        return res[0]
            
        
        
    def inorder(self,node,res):
        if not node:
            return 
        self.inorder(node.left,res)
        res.append(node)
        self.inorder(node.right,res)
        
    
# Time complexity is O(N)

# Space complexity is O(N)

