// Given the root of a binary tree, return its maximum depth.

// A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

var maxDepth = function (root) {
  if (root === null) return 0;
  let left = maxDepth(root.left);
  let right = maxDepth(root.right);
  return Math.max(left, right) + 1;
};

// time complexity is O(n) where n is the number of nodes in the tree

// the space complexity in the worst case is O(n) and in the best case, a perfectly balanced tree, is O(log N)
