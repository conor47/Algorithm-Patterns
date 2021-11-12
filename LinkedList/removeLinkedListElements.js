// Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

// Input: head = [1,2,6,3,4,5,6], val = 6
// Output: [1,2,3,4,5]

// Example 2:

// Input: head = [], val = 1
// Output: []

// Example 3:

// Input: head = [7,7,7,7], val = 7
// Output: []

// Constraints:

//     The number of nodes in the list is in the range [0, 104].
//     1 <= Node.val <= 50
//     0 <= val <= 50

const removeElements = function (head, val) {
  if (head === null) return null;

  let current = head;
  let next;
  while (current) {
    if (current === head && current.val === val) {
      next = current.next;
      current.next = null;
      current = next;
      head = current;
      continue;
    } else if (current.next && current.next.val === val) {
      next = current.next;
      while (next && next.val === val) {
        next = next.next;
      }

      current.next = next;
      current = next;
      continue;
    }
    if (current === null) {
      break;
    }
    current = current.next;
  }
  return head;
};

// Time complexity is O(N)

// space complexity is O(1)
