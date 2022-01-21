# A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

# Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.

# Implement the CBTInserter class:

#     CBTInserter(TreeNode root) Initializes the data structure with the root of the complete binary tree.
#     int insert(int v) Inserts a TreeNode into the tree with value Node.val == val so that the tree remains complete, and returns the value of the parent of the inserted TreeNode.
#     TreeNode get_root() Returns the root node of the tree.

class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def insert(self, val: int) -> int:
        q = deque()
        q.append(self.root)
        newNode = TreeNode(val)
        
        while q:
            node = q.popleft()
            
            if node.left and node.right:
                q.append(node.left)
                q.append(node.right)
            
            if not node.left:
                node.left = newNode 
                return node.val
            
            elif not node.right:
                node.right = newNode
                return node.val 

# Time complexity is O(N)

# Space complexity is O(N)