// Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

// Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
// Output: 32
// Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

const rangeSumBST = function (root, low, high) {
  let sum = 0;

  const recursive = function (node, low, high) {
    if (node === null) {
      return;
    }

    if (node.val <= high && node.val >= low) {
      sum += node.val;
    }

    if (node.left) {
      recursive(node.left, low, high);
    }
    if (node.right) {
      recursive(node.right, low, high);
    }
  };
  recursive(root, low, high);
  return sum;
};

// Time complexity is O(N) since we are using DFS to visit every node
// Space complexity is O(N) since in the worst case where the tree is a linked list
// the call stack will be N high

// single recursive function solution

const rangeSumBST = function (root, low, high) {
  if (root === null) {
    return 0;
  }

  if (root.val < low || root.val > high) {
    return (
      0 + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high)
    );
  }

  return (
    root.val +
    rangeSumBST(root.left, low, high) +
    rangeSumBST(root.right, low, high)
  );
};
