// Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest path between any two leaf nodes. The diameter of a tree may or may not pass through the root.

// Note: You can always assume that there are at least two leaf nodes in the given tree.

class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class TreeDiameter {
  constructor() {
    this.treeDiameter = 0;
  }

  find_diameter(root) {
    this.calculate_height(root);
    return this.treeDiameter;
  }

  calculate_height(currentNode) {
    if (currentNode === null) return 0;

    let leftHeight = this.calculate_height(currentNode.left);
    let rightHeight = this.calculate_height(currentNode.right);

    if (leftHeight !== 0 && rightHeight !== 0) {
      let tempDiameter = leftHeight + rightHeight + 1;
      this.treeDiameter = Math.max(this.treeDiameter, tempDiameter);
    }

    return Math.max(leftHeight, rightHeight) + 1;
  }
}

// time complexity is O(N) since we are visiting every node in the tree

// space complexity is O(N) for the recursion stack. In the worst case the tree is maximally skewed ie a linked list

var treeDiameter = new TreeDiameter();
var root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3);
root.left.left = new TreeNode(4);
root.right.left = new TreeNode(5);
root.right.right = new TreeNode(6);
console.log(`Tree Diameter: ${treeDiameter.find_diameter(root)}`);
root.left.left = null;
root.right.left.left = new TreeNode(7);
root.right.left.right = new TreeNode(8);
root.right.right.left = new TreeNode(9);
root.right.left.right.left = new TreeNode(10);
root.right.right.left.left = new TreeNode(11);
console.log(`Tree Diameter: ${treeDiameter.find_diameter(root)}`);
