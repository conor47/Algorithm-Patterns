// Given a binary tree, connect each node with its level order successor. The last node of each level should point to the first node of the next level.

const Dequeue = require('collections/deque');

class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  // tree traversal using 'next' pointer
  print_tree() {
    let result = "Traversal using 'next' pointer: ";
    let current = this;
    while (current != null) {
      result += current.value + ' ';
      current = current.next;
    }
    console.log(result);
  }
}

const connect_all_siblings = function (root) {
  let queue = new Dequeue();
  queue.push(root);
  while (queue.length) {
    let levelLength = queue.length;
    for (let i = 0; i < levelLength; i++) {
      let current = queue.shift();

      if (current.left) {
        queue.push(current.left);
      }
      if (current.right) {
        queue.push(current.right);
      }

      if (i <= levelLength - 2) {
        current.next = queue.peek();
      } else if (i === levelLength - 1 && queue.length > 0) {
        current.next = queue.peek();
      } else {
        current.next = null;
      }
    }
  }
};

// Time complexity is O(N)

// Space complexity is O(N)

var root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(9);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);
connect_all_siblings(root);
root.print_tree();
