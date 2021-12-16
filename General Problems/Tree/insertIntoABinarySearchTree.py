# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        newNode = TreeNode(val)
        if not node:
            return newNode
        while node:
            if val < node.val:
                if node.left:
                    node = node.left
                    continue
            elif val > node.val:
                if node.right:
                    node = node.right
                    continue
            break
        newNode = TreeNode(val)
        if val > node.val:
            node.right = newNode
        else:
            node.left = newNode
        return root
            
# Time complexity is O(Log N)

# Space complexity is O(1)
