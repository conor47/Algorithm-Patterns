// Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.

// If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

class Node {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }

  print_list() {
    let temp = this;
    while (temp !== null) {
      process.stdout.write(`${temp.value} `);
      temp = temp.next;
    }
    console.log();
  }
}
const reverse_alternate_k_elements = function (head, k) {
  if (k === null || k <= 1) {
    return head;
  }

  let current = head;
  let prev = null;

  while (current !== null) {
    let lastOfPrev = prev;
    let lastOfSubList = current;
    let next = null;
    let i = 0;

    //   perform reversal
    while (current && i < k) {
      next = current.next;
      current.next = prev;
      prev = current;
      current = next;
      i += 1;
    }

    //   link the reversed sublist
    if (lastOfPrev !== null) {
      lastOfPrev.next = prev;
    } else {
      head = prev;
    }

    // connect with the next part
    lastOfSubList.next = current;

    i = 0;

    // loop k eleememts ahead
    while (i < k && current) {
      prev = current;
      current = current.next;
      i += 1;
    }
  }
  return head;
};

const head = new Node(1);
head.next = new Node(2);
head.next.next = new Node(3);
head.next.next.next = new Node(4);
head.next.next.next.next = new Node(5);
head.next.next.next.next.next = new Node(6);
head.next.next.next.next.next.next = new Node(7);
head.next.next.next.next.next.next.next = new Node(8);

process.stdout.write('Nodes of original LinkedList are: ');
head.print_list();
result = reverse_alternate_k_elements(head, 2);
process.stdout.write('Nodes of reversed LinkedList are: ');
result.print_list();
