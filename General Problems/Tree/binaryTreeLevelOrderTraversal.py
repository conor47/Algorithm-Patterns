# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# /**
#  * Definition for a binary tree node.
#  * function TreeNode(val, left, right) {
#  *     this.val = (val===undefined ? 0 : val)
#  *     this.left = (left===undefined ? null : left)
#  *     this.right = (right===undefined ? null : right)
#  * }
#  */
# /**
#  * @param {TreeNode} root
#  * @return {number[][]}
#  */

# The iterative solution using a queue is straightforward. Below is the recursive solution which is slightly less intuitive

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = []

        if not root:
            return levels

        def helper(node,level):
            if level == len(levels):
                levels.append([])
            levels[level].append(node.val)
            
            if node.left:
                helper(node.left,level + 1)
                
            if node.right:
                helper(node.right,level + 1)
        helper(root,0)
        return levels

# Time complexity is O(N)

# Space complexity is O(N)