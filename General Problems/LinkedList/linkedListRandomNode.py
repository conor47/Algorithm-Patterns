# Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

# Implement the Solution class:

#     Solution(ListNode head) Initializes the object with the integer array nums.
#     int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be choosen.

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head    
        self.nodes = {} 
        self.length = 0
        self.getNodes(head)

    def getRandom(self) -> int:
        x = randrange(0,self.length)
        return self.nodes[x].val
        
    def getNodes(self,head):
        cur = head
        idx = 0
        while cur:
            self.nodes[idx] = cur
            self.length += 1
            idx += 1
            cur = cur.next

# Time complexity of initialisation is O(N) where N is the length of the linked list. Time complexity of getRandom is O(1)

# Space complexity is O(N)