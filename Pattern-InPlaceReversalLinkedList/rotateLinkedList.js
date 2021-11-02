// Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.

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

const rotate = function (head, rotations) {
  if (head === null || head.next === null || rotations <= 0) {
    return head;
  }

  // find length and last node of list
  let list_length = 1;
  let last_node = head;
  while (last_node.next !== null) {
    last_node = last_node.next;
    list_length += 1;
  }
  last_node.next = head;
  rotations = rotations % list_length;
  let skip_length = list_length - rotations;
  let last_node_of_rotated_list = head;
  for (let i = 0; i < skip_length - 1; i++) {
    last_node_of_rotated_list = last_node_of_rotated_list.next;
  }
  head = last_node_of_rotated_list.next;
  last_node_of_rotated_list.next = null;

  return head;
};

// Time complexity is O(n)

// Space complexity is O(1)

head = new Node(1);
head.next = new Node(2);
head.next.next = new Node(3);
head.next.next.next = new Node(4);
head.next.next.next.next = new Node(5);
head.next.next.next.next.next = new Node(6);

console.log(`Nodes of original LinkedList are: ${head.get_list()}`);
console.log(`Nodes of rotated LinkedList are: ${rotate(head, 3).get_list()}`);
