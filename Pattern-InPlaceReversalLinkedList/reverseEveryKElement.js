// Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.

// If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

class Node {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }

  get_list() {
    let result = '';
    let temp = this;
    while (temp !== null) {
      result += temp.value + ' ';
      temp = temp.next;
    }
    return result;
  }
}

const reverse_every_k_elements = function (head, k) {
  if (k === null || k <= 1) {
    return head;
  }

  let current = head;
  let previous = null;
  while (true) {
    //   storing the last node of the previous sublist so that we can connect it later on
    let lastNodeOfPrevious = previous;
    // storing the future last node of the sublist we are about to reverse
    let lastNodeOfSubList = current;
    let next = null;
    let i = 0;
    while (current && i < k) {
      next = current.next;
      current.next = previous;
      previous = current;
      current = next;
      i += 1;
    }

    // connect the previous part
    if (lastNodeOfPrevious !== null) {
      lastNodeOfPrevious.next = previous;
    } else {
      head = previous;
    }

    lastNodeOfSubList.next = current;

    if (current === null) {
      break;
    }
    previous = lastNodeOfSubList;
  }
  return head;
};

// Time complexity is O(N) where N is the number of nodes in the linked list
// Space complexity is O(1)

head = new Node(1);
head.next = new Node(2);
head.next.next = new Node(3);
head.next.next.next = new Node(4);
head.next.next.next.next = new Node(5);
head.next.next.next.next.next = new Node(6);
head.next.next.next.next.next.next = new Node(7);
head.next.next.next.next.next.next.next = new Node(8);

console.log(`Nodes of original LinkedList are: ${head.get_list()}`);
console.log(
  `Nodes of reversed LinkedList are: ${reverse_every_k_elements(
    head,
    3
  ).get_list()}`
);
