// Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

// Input: root = [1,2,2,3,4,4,3]
// Output: true

// Input: root = [1,2,2,null,3,null,3]
// Output: false

// Constraints:

//     The number of nodes in the tree is in the range [1, 1000].
//     -100 <= Node.val <= 100

var isSymmetric = function (root) {
  if (root === null) {
    return true;
  }
  return recursive(root.left, root.right);
};

const recursive = function (i, j) {
  if (i === null || j === null) {
    return i === j;
  }

  if (i.val !== j.val) {
    return false;
  }

  return recursive(i.left, j.right) && recursive(i.right, j.left);
};

// Time complexity is O(N) where N is the number of nodes in the tree

// Space complexity is O(N). The number of recursive calls is bound by the height of the tree and in the worst case the tree is linear and the
// the height is in O(N) k
