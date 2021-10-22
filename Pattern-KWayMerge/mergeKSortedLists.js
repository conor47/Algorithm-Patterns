// Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

// Example 1:

// Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
// Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]

// Example 2:

// Input: L1=[5, 8, 9], L2=[1, 7]
// Output: [1, 5, 7, 8, 9]

const heap = require('collections/heap');

class ListNode {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }
}

const merge_lists = function (lists) {
  let minHeap = new heap([], null, (a, b) => b.value - a.value);

  lists.forEach((node) => {
    if (node !== null) minHeap.push(node);
  });

  let resultHead = null;
  let resultTail = null;
  while (minHeap.length > 0) {
    let node = minHeap.pop();
    if (resultHead === null) {
      resultHead = resultTail = node;
    } else {
      resultTail.next = node;
      resultTail = resultTail.next;
    }
    if (node.next !== null) {
      minHeap.push(node.next);
    }
  }

  return resultHead;
};

l1 = new ListNode(2);
l1.next = new ListNode(6);
l1.next.next = new ListNode(8);

l2 = new ListNode(3);
l2.next = new ListNode(6);
l2.next.next = new ListNode(7);

l3 = new ListNode(1);
l3.next = new ListNode(3);
l3.next.next = new ListNode(4);

result = merge_lists([l1, l2, l3]);
output = 'Here are the elements form the merged list: ';
while (result != null) {
  output += result.value + ' ';
  result = result.next;
}
console.log(output);
