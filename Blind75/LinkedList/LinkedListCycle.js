// Given head, the head of a linked list, determine if the linked list has a cycle in it.

// There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

// Return true if there is a cycle in the linked list. Otherwise, return false.

let hasCycle = function (head) {
  if (head === null) return false;

  let fast = head;
  let slow = head;
  // note that the second null check is necessary since we we run over the end of the linked list and try to access .next on undefined
  // an typeerror will be thrown
  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) return true;
  }
  return false;
};

// time complexity is O(N+K) which is asymptotically equivalent to O(N)

// space complexity is O(1)

// An alternative solution is to use a hashmap to store the memory addresses of the nodes we have visited.
