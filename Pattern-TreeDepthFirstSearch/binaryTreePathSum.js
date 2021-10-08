// Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node
//  values of that path equals ‘S’.

class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

const has_path = function (root, sum) {
  if (root === null) return false;

  if (root.val === sum && root.left === null && root.right === null)
    return true;

  return (
    hasPath(root.left, sum - root.val) || hasPath(root.right, sum - root.val)
  );
};

// Time complexity is O(N) where N is the number of nodes in the tree

// Space complexity is O(N). This space is used to store the call stack. The worst case scenario is a linked list

var root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(9);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);
console.log(`Tree has path: ${has_path(root, 23)}`);
console.log(`Tree has path: ${has_path(root, 16)}`);
