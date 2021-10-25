class Node {
  // constructor
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  // constrictor
  constructor() {
    this.head = null;
  }

  // function for appending a new node in the linked list
  appendNode(newData) {
    let newNode = new Node(newData);
    if (this.head == null) {
      this.head = newNode;
      return;
    }

    var last = this.head;
    while (last.next != null) {
      last = last.next;
    }
    last.next = newNode;
  }

  //function for printing the linked list
  printList() {
    let temp = this.head;
    while (temp != null) {
      console.log(temp.data);
      temp = temp.next;
    }
  }
}

function length(testVariable, head) {
  if (head === null) return 0;

  if (head.next === null) return 1;

  return 1 + length(testVariable, head.next);
}

var list = new LinkedList();
list.appendNode(4);
list.appendNode(3);
list.appendNode(11);
list.appendNode(7);
console.log(length(list, list.head));
