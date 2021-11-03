// Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum.

// A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root. The path must contain at least one node.

class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class MaximumPathSum {
  find_max_path_sum(root) {
    this.globalMax = -Infinity;
    this.find_max_sum_recursive(root);
    return this.globalMax;
  }

  find_max_sum_recursive(currentNode) {
    if (currentNode === null) return 0;

    let maxPathSumLeft = this.find_max_sum_recursive(currentNode.left);
    let maxPathSumRight = this.find_max_sum_recursive(currentNode.right);

    maxPathSumLeft = Math.max(maxPathSumLeft, 0);
    maxPathSumRight = Math.max(maxPathSumRight, 0);

    let localMaxPathSum = maxPathSumLeft + maxPathSumRight + currentNode.value;

    this.globalMax = Math.max(localMaxPathSum, this.globalMax);

    return Math.max(maxPathSumLeft, maxPathSumRight) + currentNode.value;
  }
}

// Time complexity is O(N) since we are visiting every node in the tree

// Space complexity is O(N) for the recursion stack. This would occur when the tree is a linked list ie maximally skewed

const maximumPathSum = new MaximumPathSum();
let root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3);

console.log(`Maximum Path Sum: ${maximumPathSum.find_max_path_sum(root)}`);
root.left.left = new TreeNode(1);
root.left.right = new TreeNode(3);
root.right.left = new TreeNode(5);
root.right.right = new TreeNode(6);
root.right.left.left = new TreeNode(7);
root.right.left.right = new TreeNode(8);
root.right.right.left = new TreeNode(9);
console.log(`Maximum Path Sum: ${maximumPathSum.find_max_path_sum(root)}`);

root = new TreeNode(-1);
root.left = new TreeNode(-3);
console.log(`Maximum Path Sum: ${maximumPathSum.find_max_path_sum(root)}`);
