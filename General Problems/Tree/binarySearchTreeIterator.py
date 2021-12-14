# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

#     BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
#     boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
#     int next() Moves the pointer to the right, then returns the number at the pointer.

# Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

# You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.sorted = []
        self.pos = -1
        self.inorder(root)
        
    def inorder(self,node):
        if not node:
            return
        self.inorder(node.left)
        self.sorted.append(node.val)
        self.inorder(node.right)

    def next(self) -> int:
        self.pos += 1
        return self.sorted[self.pos]

    def hasNext(self) -> bool:
        return not self.pos == len(self.sorted) - 1

# Time complexity is O(N) where N is the number of nodes in the tree

# Space complexity is O(N)

# Iterative solution using custom stack

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.helper(root)

    def helper(self,node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.helper(node.right)
        return node.val
            

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Time complexity of the hasNext operation is O(1). Time complexity of the next operation is 
# on average O(1) but in some cases O(N). Its amortized time complexity is O(1)