// Given the root of a complete binary tree, return the number of the nodes in the tree.

// According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

// Design an algorithm that runs in less than O(n) time complexity.

// Naieve solution. Does not run in less than O(N) time

const countNodes = function (root) {
  return recursive(root);
};

const recursive = function (node) {
  if (node === null) {
    return 0;
  } else {
    return 1 + recursive(node.left) + recursive(node.right);
  }
};

// Time complexity is O(N)

// Space complexity is O(Log N) ie the depth of the tree.
