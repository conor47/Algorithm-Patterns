// Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

// Recursively

const swapPairs = function (head) {
  if (head === null || head.next === null) {
    return head;
  }

  let firstNode = head;
  let secondNode = head.next;

  firstNode.next = swapPairs(secondNode.next);
  secondNode.next = firstNode;

  return secondNode;
};

// Time complexity is O(N)

// Space complexity is O(N)

// Iteratively

const swapPairsV2 = function (head) {
  if (head === null || head.next === null) {
    return head;
  }

  let dummy = new ListNode(-1);
  dummy.next = head;
  let prev = dummy;

  while (head !== null && head.next !== null) {
    let firstNode = head;
    let secondNode = head.next;

    prev.next = secondNode;
    firstNode.next = secondNode.next;
    secondNode.next = firstNode;

    prev = firstNode;
    head = firstNode.next;
  }
  return dummy;
};

// Time complexity is O(N)

// Space complexity is O(1)
