// Given a binary tree and a node, find the level order successor of the given node in the tree.
// The level order successor is the node that appears right after the given node in the level order traversal.

class TreeNode {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const find_successor = function (root, key) {
  if (root === null) return result;
  let queue = [];
  let current = root;
  queue.unshift(current);
  while (queue.length) {
    current = queue.pop();

    if (current.left !== null) {
      queue.unshift(current.left);
    }
    if (current.right !== null) {
      queue.unshift(current.right);
    }
    if (current.val === key) break;
  }
  if (queue.length) {
    return queue.pop().val;
  }
  return null;
};

// Time complexity is O(N)

// Space complexity is O(N) since we used a queue. We can have a maximum of N/2 nodes at any level , which only happens at the lowest level

var root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(9);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);
result = find_successor(root, 12);
if (result !== null) console.log(result.val);
result = find_successor(root, 9);
if (result !== null) console.log(result.val);
