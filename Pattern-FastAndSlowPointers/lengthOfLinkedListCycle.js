// Problem 1: Given the head of a LinkedList with a cycle, find the length of the cycle.

class Node {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }
}

function lengthOfCycle(head) {
  let fast = head;
  let slow = head;

  while (fast.next !== null && fast !== null) {
    fast = fast.next.next;
    slow = slow.next;

    if (fast === slow) {
      return calculateCycleLength(slow);
    }
  }
  return 0;
}

// secondary function for calculating cycle length once a cycle has been detected

function calculateCycleLength(slow) {
  let current = slow;
  let count = 0;

  while (true) {
    current = current.next;
    count += 1;
    if (current === slow) {
    }
  }
  return count;
}
