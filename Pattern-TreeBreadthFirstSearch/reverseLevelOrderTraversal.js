// Given a binary tree, populate an array to represent its level-by-level traversal in reverse order,
// i.e., the lowest level comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.

class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// Note for simplicity sake I am using an array to model a basic queue. This is not efficient. A more efficient approach would be
// to use a linked list or external collections library and use a dequeue etc

const traverse = function (root) {
  result = [];
  if (root === null) return result;
  let queue = [];
  let current = root;
  queue.unshift(current);
  while (queue.length) {
    let levelSize = queue.length;
    let currentLevel = [];
    for (let i = 0; i < levelSize; i++) {
      current = queue.pop();
      currentLevel.push(current.value);
      if (current.left !== null) {
        queue.unshift(current.left);
      }
      if (current.right !== null) {
        queue.unshift(current.right);
      }
    }
    result.unshift(currentLevel);
  }
  return result;
};

var root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(9);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);
console.log(`Reverse level order traversal: ${traverse(root)}`);
