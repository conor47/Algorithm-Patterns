# You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

# Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

# Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

# Iterative solution using a stack

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        dummy = Node(0,None,head,None)
        prev = dummy
        
        stack = []
        stack.append(head)
        
        while stack:
            curr = stack.pop()
            
            prev.next = curr
            curr.prev = prev
            
            if curr.next:
                stack.append(curr.next)
            
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            prev = curr
        dummy.next.prev = None
        return dummy.next
        
        
# Time complexity is O(N)
# Space complexity O(N)

# Recursive solution

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        
        self.dfs(head)
        return head
    
    def dfs(self,node):
        
        while node:
            
            curr_next = node.next
            if not curr_next:
                tail = node

            if node.child:
                node.next = node.child
                node.child.prev = node
                child_tail = self.dfs(node.child)

                if curr_next:
                    curr_next.prev = child_tail
                child_tail.next = curr_next
                node.child = None
            node = node.next
        return tail

