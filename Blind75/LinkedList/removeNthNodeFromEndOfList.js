// Given the head of a linked list, remove the nth node from the end of the list and return its head

// Input: head = [1,2,3,4,5], n = 2
// Output: [1,2,3,5]

// Example 2:

// Input: head = [1], n = 1
// Output: []

// Example 3:

// Input: head = [1,2], n = 1
// Output: [1]

// Constraints:

//     The number of nodes in the list is sz.
//     1 <= sz <= 30
//     0 <= Node.val <= 100
//     1 <= n <= sz

let removeNthFromEnd = function (head, n) {
  //     find length
  let dummyHead = new ListNode(0);
  dummyHead.next = head;
  let temp = head;
  let length = 0;
  while (temp) {
    length += 1;
    temp = temp.next;
  }

  length -= n;
  temp = dummyHead;
  while (length > 0) {
    length -= 1;
    temp = temp.next;
  }

  temp.next = temp.next.next;
  return dummyHead.next;
};

// Time complexity is O(N) where n is the number of nodes in the linked list

// space complexity is O(1)

// Alternative solution solving in one pass of the linked list

let removedHeadV2 = function (head, n) {
  let dummyHead = new ListNode(0);
  let first = dummyHead;
  let second = dummyHead;
  // move first n nodes ahead of second. There should be n nodes between first and second
  for (let i = 0; i <= n; i++) {
    first = first.next;
  }

  while (first !== null) {
    first = first.next;
    second = second.next;
  }

  second.next = second.next.next;
  return dummyHead.next;
};
