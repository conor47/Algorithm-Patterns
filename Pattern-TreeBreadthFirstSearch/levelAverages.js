// Given a binary tree, populate an array to represent the averages of all of its levels.

class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

const find_level_averages = function (root) {
  result = [];
  if (root === null) return result;
  let queue = [];
  let current = root;
  queue.unshift(current);
  while (queue.length) {
    let levelSize = queue.length;
    let currentLevel = 0;
    for (let i = 0; i < levelSize; i++) {
      current = queue.pop();
      currentLevel += current.value;
      if (current.left !== null) {
        queue.unshift(current.left);
      }
      if (current.right !== null) {
        queue.unshift(current.right);
      }
    }
    result.push(currentLevel / levelSize);
  }
  return result;
};

var root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(9);
root.left.right = new TreeNode(2);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);

console.log(`Level averages are: ${find_level_averages(root)}`);
