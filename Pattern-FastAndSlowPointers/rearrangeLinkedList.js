// Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

// Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

// Example 1:

// Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
// Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null

// Example 2:

// Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
// Output: 2 -> 10 -> 4 -> 8 -> 6 -> null

class Node {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }

  print_list() {
    let result = '';
    let temp = this;
    while (temp !== null) {
      result += temp.value + ' ';
      temp = temp.next;
    }
    console.log(result);
  }
}

const reorder = function (head) {
  let slow = head;
  let fast = head;

  //   find the middle of the linked list
  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
  }

  //   reverse the second half of the linked list
  let headSecondHalf = reverse(slow);
  let headFirstHalf = head;

  //   combine the two halfs in the correct order

  while (headFirstHalf !== null && headSecondHalf !== null) {
    let temp = headFirstHalf.next;
    headFirstHalf.next = headSecondHalf;
    headFirstHalf = temp;

    temp = headSecondHalf.next;
    headSecondHalf.next = headFirstHalf;
    headSecondHalf = temp;
  }

  //   set the last nodes next value equal to null
  if (headFirstHalf !== null) {
    headFirstHalf.next = null;
  }
};

const reverse = function (head) {
  let prev = null;
  while (head !== null) {
    let next = head.next;
    head.next = prev;
    prev = head;
    head = next;
  }
  return prev;
};

// time complexity is is O(N) where N is the number of nodes in the linked list

// Space complexity is O(1)

head = new Node(2);
head.next = new Node(4);
head.next.next = new Node(6);
head.next.next.next = new Node(8);
head.next.next.next.next = new Node(10);
head.next.next.next.next.next = new Node(12);
reorder(head);
head.print_list();
