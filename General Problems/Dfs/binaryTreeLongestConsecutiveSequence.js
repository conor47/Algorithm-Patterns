// Given the root of a binary tree, return the length of the longest consecutive sequence path.

// The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path needs to be from parent to child (cannot be the reverse).

// Input: root = [1,null,3,2,4,null,null,null,5]
// Output: 3
// Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

const longestConsecutive = function (root) {
  let max = [1];
  recursive(root, max, 0, 0);
  return max[0];
};

const recursive = function (node, max, target, count) {
  if (node === null) {
    return;
  }

  if (node.val !== target) {
    count = 0;
  }

  count += 1;
  max[0] = Math.max(count, max[0]);
  recursive(node.left, max, node.val + 1, count);
  recursive(node.right, max, node.val + 1, count);
};

// Time complexity is O(N) since we are visiting every node

// Space complexity is O(N) since in the worst case the tree is a linked list
