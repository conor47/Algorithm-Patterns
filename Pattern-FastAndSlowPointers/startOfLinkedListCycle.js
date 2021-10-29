// Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

class Node {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }
}

const find_cycle_start = function (head) {
  let fast = head;
  let slow = head;
  lengthOfCycle;

  while (fast !== null && fast.next !== null) {
    fast = fast.next.next;
    slow = slow.next;

    if (fast === slow) {
      // calculte the length of the cycle
      cycleLength = calculateCycleLength(slow);
    }
  }
  slow = head;
  fast = head;

  // move one pointer ahead of the other by the number of nodes which is the length of the cycle
  while (lengthOfCycle > 0) {
    fast = fast.next;
    lengthOfCycle--;
  }
  // loop until the pointers meet. When they meet we know we are at the head of the cycle
  while (fast !== slow) {
    fast = fast.next;
    slow = slow.next;
  }
  return fast;
};

function calculateCycleLength(slow) {
  let current = slow;
  let count = 0;

  while (true) {
    current = current.next;
    count += 1;
    if (current === slow) {
      break;
    }
  }
  return count;
}

// Time complexity is O(N). Finding the length of the cycle is O(N) and finding the head of the cycle is O(N)

// Space complexity is O(1). Constant space

head = new Node(1);
head.next = new Node(2);
head.next.next = new Node(3);
head.next.next.next = new Node(4);
head.next.next.next.next = new Node(5);
head.next.next.next.next.next = new Node(6);

head.next.next.next.next.next.next = head.next.next;
console.log(`LinkedList cycle start: ${find_cycle_start(head).value}`);

head.next.next.next.next.next.next = head.next.next.next;
console.log(`LinkedList cycle start: ${find_cycle_start(head).value}`);

head.next.next.next.next.next.next = head;
console.log(`LinkedList cycle start: ${find_cycle_start(head).value}`);
