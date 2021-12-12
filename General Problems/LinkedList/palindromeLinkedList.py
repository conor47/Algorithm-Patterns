# Given the head of a singly linked list, return true if it is a palindrome

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = []
        current = head
        while current:
            temp.append(current.val)
            current = current.next
            
        left = 0
        right = len(temp) - 1
        while left < right:
            if temp[left] != temp[right]:
                return False
            left += 1
            right -= 1
        return True

# Time complexity is O(N)

# Space complexity is O(N)

# In order to solve this is O(1) space we woulc reverse the second half of the linked list 