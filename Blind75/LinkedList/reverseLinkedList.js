// Given the head of a singly linked list, reverse the list, and return the reversed list.

class Node {
  constructor(val = 0, next = null) {
    this.val = val;
    this.next = null;
  }
}

let reverse = (head) => {
  if (head === null) return null;
  let current = head;
  let prev = null;
  let next;
  while (current !== null) {
    next = current.next;
    current.next = prev;
    prev = current;
    current = next;
  }
  return prev;
};

// time complexity is O(n)
// space complexity is O(1)

let reverseRecursive = (head) => {
  if (head === null || head.next === null) {
    return head;
  }
  let p = reverseRecursive(head.next);
  head.next.next = head;
  head.next = null;
  return p;
};
