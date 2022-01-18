# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        before = self.findNode(left,dummy)
        newTail = before.next
        after = self.findNode(right+1,head)
        before.next = self.reverse(newTail,right - left + 1)
        newTail.next = after 
        return dummy.next
        
        
        
    def findNode(self,n,head):
        temp = head
        count = 1
        while count < n and temp:
            temp = temp.next
            count += 1
       
        return temp if temp else None
        
    def reverse(self,node,count):
        temp = node
        prev = None
        nxt = None
        while count > 0:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
            count -= 1
        return prev
    
# Time complexity is O(N)

# Space complexity is O(1)