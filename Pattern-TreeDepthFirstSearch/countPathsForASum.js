// Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’. Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).

const Dequeue = require('collections/deque');

class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

const count_paths = function (root, S) {
  if (root === null) return 0;
  return count_paths_recursive(root, S, new Dequeue());
};

const count_paths_recursive = function (currentNode, S, currentPath) {
  if (currentNode === null) {
    return 0;
  }

  currentPath.push(currentNode.value);
  let pathSum = 0;
  let pathCount = 0;

  for (let i = currentPath.length - 1; i >= 0; i--) {
    pathSum += currentPath[i];
    if (pathSum === S) {
      pathCount += 1;
    }
  }

  pathCount += count_paths_recursive(currentNode.left, S, currentPath);
  pathCount += count_paths_recursive(currentNode.right, S, currentPath);

  currentPath.pop();
  return pathCount;
};

var root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(4);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);
console.log(`Tree has paths: ${count_paths(root, 11)}`);
