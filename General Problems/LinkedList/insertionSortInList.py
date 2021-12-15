# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

# The steps of the insertion sort algorithm:

#     Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
#     At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
#     It repeats until no input elements remain.

# The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.


# First Naieve solution. TLEs on last test case

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        temp = head
        temp.prev = None
        while temp.next:
            temp.next.prev = temp
            temp = temp.next
        
        temp = head.next
        while temp:
            next = temp.next
            while temp.prev and temp.val < temp.prev.val:
                pre =  temp.prev
                if pre.prev:
                    pre.prev.next = temp
                if temp.next:
                    temp.next.prev = pre
                pre.next = temp.next
                temp.prev = pre.prev
                temp.next = pre
                pre.prev = temp
            temp = next
            
        while head.prev:
            head = head.prev
        return head 

# Time complexity is O(N(N+1)/2) which is O(N^2) 

# Space complexity is O(1)

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head
        
        while curr:
            prev = dummy
            
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
                
            next = curr.next
            curr.next = prev.next
            prev.next = curr
            
            curr = next
        return dummy.next

# Time complexity is O(N^2)

# Space complexity is O(1)