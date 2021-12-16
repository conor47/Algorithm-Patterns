# Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.

# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        heap = []
        self.recurse(root,heap,k,target)
        return [val for diff,val in heap]
        
        
        
    def recurse(self,node,heap,k,target):
        if not node:
            return
        diff = abs(target - node.val)
        heapq.heappush(heap,(-diff,node.val))
        if len(heap) > k:
            heapq.heappop(heap)
        if node.left:
            self.recurse(node.left,heap,k,target)
        if node.right:
            self.recurse(node.right, heap,k,target)

# Time complexity is O(N LogK)

# Space complexity is O(N + K) or O(H + K) for the heap and the recursion stackit
