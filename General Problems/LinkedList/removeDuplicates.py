# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        slow = head
        fast = head
        while fast:
            while fast and fast.val == slow.val:
                fast = fast.next
            slow.next = fast
            slow = fast
        return head

# Time complexity is O(N)

# Space complexity is O(1)