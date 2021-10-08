// Given a binary tree, populate an array to represent its zigzag level order traversal.
// You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.

const e = require('express');

class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

const traverse = function (root) {
  result = [];
  if (root === null) return result;
  let queue = [];
  let current = root;
  let leftToRight = true;
  queue.unshift(current);
  while (queue.length) {
    let levelSize = queue.length;
    let currentLevel = [];
    for (let i = 0; i < levelSize; i++) {
      current = queue.pop();
      if (leftToRight) {
        currentLevel.push(current.value);
      } else {
        currentLevel.unshift(current.value);
      }
      if (current.left !== null) {
        queue.unshift(current.left);
      }
      if (current.right !== null) {
        queue.unshift(current.right);
      }
    }
    result.push(currentLevel);
    leftToRight = !leftToRight;
  }
  return result;
};

// Time complexity is O(N) where N is the total number of nodes in the tree

// Space complexity is O(N)

var root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(9);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);
root.right.left.left = new TreeNode(20);
root.right.left.right = new TreeNode(17);
console.log(`Zigzag traversal: ${traverse(root)}`);
