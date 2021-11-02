// Given a binary tree, populate an array to represent the averages of all of its levels.

class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

const find_level_averages = function (root) {
  let result = [];
  if (root === null) return result;
  let queue = [root];
  while (queue.length) {
    let levelSize = queue.length;
    let currentLevel = 0;
    for (let i = 0; i < levelSize; i++) {
      current = queue.shift();
      currentLevel += current.value;
      if (current.left) {
        queue.push(current.left);
      }
      if (current.right) {
        queue.push(current.right);
      }
    }
    result.push(currentLevel / levelSize);
  }
  return result;
};

var root = new TreeNode(3);
root.left = new TreeNode(9);
root.right = new TreeNode(20);
root.left.left = new TreeNode(null);
root.left.right = new TreeNode(null);
root.right.left = new TreeNode(15);
root.right.right = new TreeNode(7);

console.log(`Level averages are: ${find_level_averages(root)}`);
