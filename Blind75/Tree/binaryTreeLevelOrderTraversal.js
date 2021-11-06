// Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

let levelOrder = function (root) {
  if (root === null) return [];
  let result = [];
  let queue = [root];
  let current;
  let levelSize;
  while (queue.length > 0) {
    let levelOrder = [];
    levelSize = queue.length;
    for (let i = 0; i < levelSize; i++) {
      current = queue.shift();
      levelOrder.push(current.val);
      if (current.left) queue.push(current.left);
      if (current.right) queue.push(current.right);
    }
    result.push(levelOrder);
  }
  return result;
};

// time complexity is O(N)

// space complexity is O(N) for queue

let levelOrderRecursive = function (root) {
  let levels = [];

  let helper = function (node, level) {
    if (level === levels.length) {
      levels.push([]);
    }
    levels[level].push(node.val);

    if (node.left) {
      helper(node.left, level + 1);
    }
    if (node.right) {
      helper(node.right, level + 1);
    }
  };
  helper(root, 0);
  return levels;
};
