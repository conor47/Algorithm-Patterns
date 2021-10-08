// Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.

class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function find_paths(root, sum) {
  return findPathsRecursive(root, sum, [], []);
}

function findPathsRecursive(currentNode, sum, currentPath, allPaths) {
  if (!currentNode) return;

  //   add the current node to the path
  currentPath.push(currentNode.val);

  //   we save the current path if the current node value equals the sum and its a leaf node
  if (currentNode.val === sum && !currentNode.left && !currentNode.rigth) {
    allPaths.push(currentPath.slice());
  } else {
    //   Traverse the left subtree
    findPathsRecursive(
      currentNode.left,
      sum - currentNode.val,
      currentPath,
      allPaths
    );
    //   Traverse the right subtree
    findPathsRecursive(
      currentNode.right,
      sum - currentNode.val,
      currentPath,
      allPaths
    );
  }
  // as we backtrack we remove the current node from the path
  currentPath.pop();
  return allPaths;
}

//

const root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(4);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);
let sum = 23,
  result = find_paths(root, sum);

process.stdout.write(`Tree paths with sum ${sum}: `);
for (i = 0; i < result.length; i++) {
  process.stdout.write(`[${result[i]}] `);
}
