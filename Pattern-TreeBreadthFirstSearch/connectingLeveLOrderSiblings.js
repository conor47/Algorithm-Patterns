// Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.

const Dequeue = require('collections/deque');

class TreeNode {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
    this.next = null;
  }

  // level order traversal using 'next' pointer
  print_level_order() {
    console.log("Level order traversal using 'next' pointer: ");
    let nextLevelRoot = this;
    while (nextLevelRoot !== null) {
      let current = nextLevelRoot;
      nextLevelRoot = null;
      while (current != null) {
        process.stdout.write(`${current.val} `);
        if (nextLevelRoot === null) {
          if (current.left !== null) {
            nextLevelRoot = current.left;
          } else if (current.right !== null) {
            nextLevelRoot = current.right;
          }
        }
        current = current.next;
      }
      console.log();
    }
  }
}

const connect_level_order_siblings = function (root) {
  let queue = new Dequeue();
  queue.push(root);
  while (queue.length) {
    let levelLength = queue.length;
    for (let i = 0; i < levelLength; i++) {
      let current = queue.shift();
      if (i <= levelLength - 2) {
        current.next = queue.peek();
      } else {
        current.next = null;
      }
      if (current.left) {
        queue.push(current.left);
      }
      if (current.right) {
        queue.push(current.right);
      }
    }
  }
};

// Time complexity is O(N)

// Space complexity is O(N). The maximum number of nodes we can have at a level is N/2, which can occur at the bottom level

var root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(9);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);
connect_level_order_siblings(root);

root.print_level_order();
