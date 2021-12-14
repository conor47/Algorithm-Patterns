# The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

# The left boundary is the set of nodes defined by the following:

#     The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
#     If a node in the left boundary and has a left child, then the left child is in the left boundary.
#     If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
#     The leftmost leaf is not in the left boundary.

# The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

# The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

# Given the root of a binary tree, return the values of its boundary.

# solution passes all test cases but TLEs

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        elif n == 1:
            return [TreeNode(0)]
        ans = []
        for i in range(n):
            y = n - 1 - i
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(y):
                    bns = TreeNode(0)
                    bns.left = left
                    bns.right = right
                    ans.append(bns)
        return ans

# using memoization

class Solution:
    memo = {0:[], 1:[TreeNode(0)]}
    
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n not in self.memo:
            ans = []
            for i in range(n):
                y = n - 1 - i
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            self.memo[n] = ans
        return self.memo[n]

# Time complexity is O(2^n)

# Space complexity is O(2^n) 

