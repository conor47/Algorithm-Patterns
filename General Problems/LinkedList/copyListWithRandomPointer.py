# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

#     val: an integer representing Node.val
#     random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

# Your code will only be given the head of the original linked list.

# First naive solution, a faster solution would involve using a hash map to maintain the position of each node in the list

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0) 
        temp = head
        cur = dummy
        l = 0
        while temp:
            cur.next = Node(temp.val)
            temp = temp.next
            cur = cur.next
            l += 1
        cur.next = None
        cur = dummy.next
        temp = head
        while temp:
            n = temp.random
            if n:
                cur.random = self.findNode(n,dummy.next,head)
            temp = temp.next
            cur = cur.next
        return dummy.next
        
    def findNode(self,n,newHead,oldHead):
        temp = oldHead
        count = 0
        while temp != n:
            count += 1
            temp = temp.next
        temp = newHead
        while count > 0:
            temp=temp.next
            count -= 1
        return temp