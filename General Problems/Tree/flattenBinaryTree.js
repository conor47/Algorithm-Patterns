// Given the root of a binary tree, flatten the tree into a "linked list":

//     The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
//     The "linked list" should be in the same order as a pre-order traversal of the binary tree.

//     Input: root = [1,2,5,3,4,null,6]
//     Output: [1,null,2,null,3,null,4,null,5,null,6]

//     Example 2:

//     Input: root = []
//     Output: []

//     Example 3:

//     Input: root = [0]
//     Output: [0]

//     Constraints:

//         The number of nodes in the tree is in the range [0, 2000].
//         -100 <= Node.val <= 100

var flatten = function (root) {
  if (root === null) {
    return null;
  }

  let stack = [root];
  while (stack.length) {
    let node = stack.pop();

    if (node.right) {
      stack.push(node.right);
    }

    if (node.left) {
      stack.push(node.left);
    }

    if (stack.length) {
      node.right = stack[stack.length - 1];
    }

    node.left = null;
  }
  return root;
};

// Time complexity is O(N)

// Space complexity is O(N) since the tree can be skewed
