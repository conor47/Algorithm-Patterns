// biven a binary tree, populate an array to represent its level-by-level traversal.
//  You should populate the values of all nodes of each level from left to right in separate sub-arrays.

class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// this is a simple bfs implementation. This does not answer the question of populating the values of each level in seperate sub-arrays

const traverse = function (root) {
  result = [];
  if (root === null) return result;
  let queue = [];
  let current = root;
  queue.unshift(current);
  while (queue.length) {
    current = queue.pop();
    result.push(current.value);
    if (current.left) {
      queue.unshift(current.left);
    }
    if (current.right) {
      queue.unshift(current.right);
    }
  }
  return result;
};

const traverseV2 = function (root) {
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
    result.push(currentLevel);
  }
  return result;
};

// time complexity  is O(N) where N is the total number of nodes the tree

// Space complexity is O(N) since we need to return a list containing the level order traversal of the tree.
// We also need O(N) space for the queue

var root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(9);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);
console.log(`Level order traversal: ${traverseV2(root)}`);
