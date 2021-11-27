# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self.dfs(root,res)
        return res
        
    def dfs(self,node,res):
        if not node:
            return
        res.append(node.val)
        for child in node.children:
            self.dfs(child,res)

# Time complexity is O(N)

# Space complexity is O(N)