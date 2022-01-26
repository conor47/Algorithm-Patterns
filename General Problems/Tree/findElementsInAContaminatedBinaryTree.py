# Given a binary tree with the following rules:

#     root.val == 0
#     If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
#     If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2

# Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

# Implement the FindElements class:

#     FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
#     bool find(int target) Returns true if the target value exists in the recovered binary tree.

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.values = set()
        self.dfs(self.root,0)

    def find(self, target: int) -> bool:
        return target in self.values
        
    def dfs(self,node,val):
        if not node:
            return
        node.val = val
        self.values.add(val)
        
        if node.left:
            self.dfs(node.left,2*val+1)
    
        if node.right:
            self.dfs(node.right,2*val+2)

# Time complexity is O(N)

# Space complexity is O(N)