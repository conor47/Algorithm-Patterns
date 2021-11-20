// Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

// A subtree of a node node is node plus every node that is a descendant of node.

// Input: root = [1,null,0,0,1]
// Output: [1,null,0,null,1]
// Explanation:
// Only the red nodes satisfy the property "every subtree not containing a 1".
// The diagram on the right represents the answer.

// Input: root = [1,0,1,0,0,0,1]
// Output: [1,null,1,null,1]

var pruneTree = function (root) {
  if (root === null) {
    return null;
  }
  return prune(root) ? root : null;
};

const prune = function (node) {
  if (node === null) {
    return false;
  }

  let left = prune(node.left);
  let right = prune(node.right);

  if (!left) {
    node.left = null;
  }
  if (!right) {
    node.right = null;
  }

  return node.val === 1 || left || right;
};

// Time complexity is O(N)

// Space complexity is O(H) where H is the height of the tree. In the worst case the space complexity will be O(N)
