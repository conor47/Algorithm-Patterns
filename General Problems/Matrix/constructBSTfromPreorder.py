# Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

# It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

# A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

# A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder) 
        idxMap = {val:idx for idx,val in enumerate(inorder)}
        
        def construct(left, right):
            if left > right:
                return None
            val = preorder.pop(0)         
            node = TreeNode(val)
            idx = idxMap[val]
            node.left = construct(left,idx - 1)
            node.right = construct(idx +1,right)
            return node
        
        return construct(0,len(preorder) - 1)

# Time complexity is O(NlogN) due to the sorting operation

# space complexity is O(N)

# Optimal solution 

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def helper(lower = float('-inf'), upper = float('inf')):
            nonlocal idx 
            if idx == n:
                return None
            
            val = preorder[idx]
            if val < lower or val > upper:
                return None
            
            idx += 1
            node = TreeNode(val) 
            node.left = helper(lower,val)
            node.right = helper(val,upper)
            return node

# time complexity is O(N)

# space complexity is O(n)