// Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.

class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

const find_minimum_depth = function (root) {
  if (root === null) return result;
  let depth = 1;
  let queue = [];
  let current = root;
  queue.unshift(current);
  while (queue.length) {
    let levelSize = queue.length;
    for (let i = 0; i < levelSize; i++) {
      current = queue.pop();
      currentLevel += current.value;
      if (current.left !== null) {
        queue.unshift(current.left);
      } else if (current.right !== null) {
        queue.unshift(current.right);
      } else {
        return depth;
      }
    }
    depth += 1;
  }
  return depth;
};

// Time and space complexity are O(N)

var root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);
console.log(`Tree Minimum Depth: ${find_minimum_depth(root)}`);
root.left.left = new TreeNode(9);
root.right.left.left = new TreeNode(11);
console.log(`Tree Minimum Depth: ${find_minimum_depth(root)}`);
