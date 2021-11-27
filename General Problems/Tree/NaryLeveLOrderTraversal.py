# Given an n-ary tree, return the level order traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        
        queue = collections.deque()
        queue.append(root)
        
        while len(queue):
            level_size = len(queue)
            level = []
            for i in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                for child in node.children:
                    queue.append(child)
            res.append([*level])
        return res

# Time complexity is O(N)

# Space complexity is O(N). At most the queue will have two layers of nodes on it at one time. In a balanced trees half or more nodes
# are often in the bottom two layers so we go with the worst space complexity of O(N)