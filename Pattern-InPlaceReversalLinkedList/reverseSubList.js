// Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.

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

const reverse_sub_list = function (head, p, q) {
  let current = head;
  let previous = null;
  let count = 0;
  //   loop up to node p
  while (count < p - 1 && current !== null) {
    previous = current;
    current = current.next;
    count += 1;
  }

  //   save the last node of the first part of the linked list and the future last node of the reversed sublist
  const lastNodeFirstPart = previous;
  const LastNodeOfSubList = current;

  let next = null;

  //   reverse the nodes between q and p
  count = 0;
  while (current !== null && count < q - p + 1) {
    next = current.next;
    current.next = previous;
    previous = current;
    current = next;
    count += 1;
  }

  // connect the first part of the linked list with the reversed sub list
  if (lastNodeFirstPart !== null) {
    lastNodeFirstPart.next = previous;
    // p = 1. We are changing the first node
  } else {
    head = previous;
  }

  //   connect the last part of the linked list with the reversed sub list

  LastNodeOfSubList.next = current;

  return head;
};

head = new Node(1);
head.next = new Node(2);
head.next.next = new Node(3);
head.next.next.next = new Node(4);
head.next.next.next.next = new Node(5);

console.log(`Nodes of original LinkedList are: ${head.get_list()}`);
console.log(
  `Nodes of reversed LinkedList are: ${reverse_sub_list(head, 2, 4).get_list()}`
);
