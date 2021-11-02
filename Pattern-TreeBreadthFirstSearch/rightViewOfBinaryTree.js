// Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.

const Dequeue = require('collections/deque');

class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

const tree_right_view = function (root) {
  result = [];
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

      if (i === levelLength - 1) {
        result.push(current.value);
      }
    }
  }
  return result;
};

// Time complexity is O(N)

// Space complexity is O(N)

var root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(9);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);
root.left.left.left = new TreeNode(3);
console.log('Tree right view: ' + tree_right_view(root));
