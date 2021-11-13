// Given the root of a binary tree, determine if it is a valid binary search tree (BST).

// A valid BST is defined as follows:

//     The left subtree of a node contains only nodes with keys less than the node's key.
//     The right subtree of a node contains only nodes with keys greater than the node's key.
//     Both the left and right subtrees must also be binary search trees.

//     Input: root = [2,1,3]
//     Output: true

//     Input: root = [5,1,4,null,null,3,6]
//     Output: false
//     Explanation: The root node's value is 5 but its right child's value is 4.

//     Constraints:

//         The number of nodes in the tree is in the range [1, 104].
//         -231 <= Node.val <= 231 - 1

const isValidBST = function (root) {
  return validate(root, null, null);
};

const validate = function (node, max, min) {
  if (node === null) {
    return true;
  } else if (
    (min !== null && node.val <= min) ||
    (max !== null && node.val >= max)
  ) {
    return false;
  }

  return (
    validate(node.left, node.val, min) && validate(node.right, max, node.val)
  );
};

// Time complexity is O(N)

// Space complexity is O(N) in the worst case we have a maximally skewed tree ie a linked list
