# import abc 
# from abc import ABC, abstractmethod 
# """
# This is the interface for the expression tree Node.
# You should not remove it, and you can define some classes to implement it.
# """

# class Node():
#     @abstractmethod
#     # define your fields here
#     def __init__(self,val):
#         self.val = val
#         self.left = None
#         self.right = None
    
#     def evaluate(self) -> int:
#         if self.val.isdigit():
#             return int(self.val)
#         left = self.left.evaluate()
#         right = self.right.evaluate()
#         if self.val == '*':
#             return left * right
#         elif self.val == '/':
#             return left // right
#         elif self.val == '+':
#             return left + right
#         else:
#             return left - right
        


# """    
# This is the TreeBuilder class.
# You can treat it as the driver code that takes the postinfix input
# and returns the expression tree represnting it as a Node.
# """

# class TreeBuilder(object):
#     def buildTree(self, postfix: List[str]) -> 'Node':
#         stack,cur = [],None
#         for c in postfix:
#             cur = Node(c)
#             if not c.isdigit():
#                 cur.right = stack.pop() 
#                 cur.left = stack.pop()
#             stack.append(cur)
#         return cur
# """
# Your TreeBuilder object will be instantiated and called as such:
# obj = TreeBuilder();
# expTree = obj.buildTree(postfix);
# ans = expTree.evaluate();
# """

import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node():
    @abstractmethod
    # define your fields here
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
    def evaluate(self) -> int:
        if self.val.isdigit():
            return int(self.val)
        left = self.left.evaluate()
        right = self.right.evaluate()
        if self.val == '*':
            return left * right
        elif self.val == '/':
            return left // right
        elif self.val == '+':
            return left + right
        else:
            return left - right
        


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack,cur = [],None
        for c in postfix:
            cur = Node(c)
            if not c.isdigit():
                cur.right = stack.pop() 
                cur.left = stack.pop()
            stack.append(cur)
        return cur
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""

