// Given the root of a binary tree, invert the tree, and return its root.

// Input: root = [4,2,7,1,3,6,9]
// Output: [4,7,2,9,6,3,1]

const invertTree = function (root) {
  const recursive = function (node) {
    if (node === null) {
      return;
    }

    if (node.left) {
      recursive(node.left);
    }
    if (node.right) {
      recursive(node.right);
    }

    let temp = node.left;
    node.left = node.right;
    node.right = temp;
  };

  recursive(root);
  return root;
};

// Time complexity is O(N) where N is the number of nodes in the tree

// Space complexity is O(H) where H is the height of the tree. Since H is an element of N, ie in the worst cast H will equal N
// the space complexity is O(N)
