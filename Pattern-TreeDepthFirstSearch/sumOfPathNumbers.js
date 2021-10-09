// Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number.
// Find the total sum of all the numbers represented by all paths.

class TreeNode {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const find_sum_of_path_numbers = function (root) {
  let result = findPathsRecursive(root, '', []);
  return result.reduce((acc, cur) => {
    acc += Number(cur);
    return acc;
  }, 0);
};

function findPathsRecursive(currentNode, currentPath, result) {
  //   sanity check
  if (currentNode === null) return;

  currentPath = currentPath + String(currentNode.val);

  //   we have reached a leaf node
  if (currentNode && currentNode.left === null && currentNode.right === null) {
    result.push(currentPath.slice());
  } else {
    //   traverse the left and right subtrees
    findPathsRecursive(currentNode.left, currentPath, result);
    findPathsRecursive(currentNode.right, currentPath, result);
  }

  currentPath = currentPath.substring(0, currentPath.length - 1);
  return result;
}

// alternative solution not involving strings

function find_sum_of_path_numbers(root) {
  return find_root_to_leaf_path_numbers(root, 0);
}

function find_root_to_leaf_path_numbers(currentNode, pathSum) {
  if (currentNode === null) return 0;

  pathSum = 10 * pathSum + currentNode.val;

  if (currentNode.left === null && currentNode.right === null) {
    return pathSum;
  }

  return (
    find_root_to_leaf_path_numbers(currentNode.left, pathSum) +
    find_root_to_leaf_path_numbers(currentNode.right, pathSum)
  );
}

// Time complexity is O(N)

// Space complexity is O(N) since we are using recursion

var root = new TreeNode(1);
root.left = new TreeNode(0);
root.right = new TreeNode(1);
root.left.left = new TreeNode(1);
root.right.left = new TreeNode(6);
root.right.right = new TreeNode(5);
console.log(`Total Sum of Path Numbers: ${find_sum_of_path_numbers(root)}`);
