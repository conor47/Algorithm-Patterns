// You are given the head of a singly linked-list. The list can be represented as:

// L0 → L1 → … → Ln - 1 → Ln

// Reorder the list to be on the following form:

// L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

// You may not modify the values in the list's nodes. Only nodes themselves may be changed.

let reorderList = function (head) {
  if (head === null) return null;
  let middle = findMiddle(head);
  let firstHead = head;
  let secondHead = reverse(middle);
  let firstTemp = firstHead;
  let secondTemp = secondHead;

  while (secondHead.next) {
    firstTemp = firstHead.next;
    firstHead.next = secondHead;
    firstHead = firstTemp;
    secondTemp = secondHead.next;
    secondHead.next = firstHead;
    secondHead = secondTemp;
  }
  return head;
};

let findMiddle = function (head) {
  let slow = head;
  let fast = head;
  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
  }
  return slow;
};

let reverse = function (head) {
  let current = head;
  let prev = null;
  let next;
  while (current) {
    next = current.next;
    current.next = prev;
    prev = current;
    current = next;
  }
  return prev;
};

// time complexity is O(N)

// space complexity is(1)
