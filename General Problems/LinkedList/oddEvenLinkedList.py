# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        def helper(first,second,second_head):
            if first.next is None or second.next is None:
                first.next = second_head
                return first
            
            first.next = first.next.next
            second.next = second.next.next
            helper(first.next,second.next, second_head)
            return first
        
        return helper(head,head.next,head.next)

# Time complexity O(N) where N is the length of the linked list

# Space complexity is O(N)

# Iterative solution. Meets problem constraints of O(1) space complexity

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        head_first = head
        head_second = head.next
        first = head
        second = first.next
        while first.next and first.next.next:
            first.next = first.next.next
            second.next = second.next = second.next.next
            first = first.next
            second = second.next
        first.next = head_second
        return head_first

# Time complexity is O(N)

# Space complexity is O(1)