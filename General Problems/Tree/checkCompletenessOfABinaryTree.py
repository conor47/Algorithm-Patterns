# Given the root of a binary tree, determine if it is a complete binary tree.

# In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        bfs = [root]
        i = 0
        
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1
        
        return not any(bfs[i:])

# Time complexity is O(N)
# Space complexity is O(N)

# Very nice solution using the fact that a heap is a always a complete binary tree and in an array representation of a heap if a node 
# has left and right children the are located at idx * 2 and idx * 2 + 1 respectively

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        total = self.countNodes(root)
        return self.helper(root,1,total)
    
    def countNodes(self,node):
        if not node:
            return 0
        
        return 1 + self.countNodes(node.left) + self.countNodes(node.right)
    
    def helper(self,node,idx,total):
        if not node:
            return True
        
        if idx > total:
            return False
        
        return self.helper(node.left,idx * 2, total) and self.helper(node.right, idx * 2 + 1,total)