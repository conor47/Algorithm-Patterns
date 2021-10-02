// Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

// Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N)O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

// Example 1:

// Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
// Output: true

// Example 2:

// Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
// Output: false

class Node {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }
}

const is_palindromic_linked_list = function (head) {
  if (head === null || head.next === null) return true;
  let slow = head;
  let fast = head;
  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
  }
  headSecondHalf = reverse(slow);
  copyHeadSecondHalf = headSecondHalf;

  while (head !== null && headSecondHalf !== null) {
    //   if this condition is true we do not have a palindrome
    if (head.value !== headSecondHalf.value) {
      break;
    }
    head = head.next;
    headSecondHalf = headSecondHalf.next;
  }

  reverse(copyHeadSecondHalf);

  if (head === null && headSecondHalf === null) {
    return true;
  }

  return false;
};

function reverse(head) {
  let prev = null;
  while (head !== null) {
    next = head.next;
    head.next = prev;
    prev = head;
    head = next;
  }
  return prev;
}

head = new Node(2);
head.next = new Node(4);
head.next.next = new Node(6);
head.next.next.next = new Node(4);
head.next.next.next.next = new Node(2);

console.log(`Is palindrome: ${is_palindromic_linked_list(head)}`);

head.next.next.next.next.next = new Node(2);
console.log(`Is palindrome: ${is_palindromic_linked_list(head)}`);
