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

function helper(linkedList, current, prev) {
  if (current.next === null) {
    linkedList.head = current;
    current.next = prev;
    return;
  }

  next = current.next;
  current.next = prev;

  helper(linkedList, next, current);
}

function reverse(myLinkedList) {
  if (myLinkedList.head === null) {
    return;
  }

  helper(myLinkedList, myLinkedList.head, null);
}

// Driver code
var list = new LinkedList();
list.appendNode(4);
list.appendNode(3);
list.appendNode(11);
list.appendNode(7);

console.log('Original Linked List:');
list.printList();

reverse(list);
console.log('\nReversed Linked List:');
list.printList();
