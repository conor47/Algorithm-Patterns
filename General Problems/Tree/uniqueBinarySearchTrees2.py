# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        
        def generate(l,r):
            
            if l == r:
                return [None]
            
            nodes = []
            for i in range(l,r):
                for left_child in generate(l,i):
                    for right_child in generate(i+1,r):
                        node = TreeNode(i+1)
                        node.left = left_child
                        node.right = right_child
                        nodes.append(node)
            return nodes
            
        return generate(0,n) if n else []