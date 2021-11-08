// Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

// Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

// Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

var serialize = function (root) {
  if (root === null) return '';
  let str = '';
  let queue = [root];
  let current;
  while (queue.length > 0) {
    current = queue.shift();
    if (current === null) {
      str += 'n' + ',';
      continue;
    }
    str += current.val + ',';
    queue.push(current.left);
    queue.push(current.right);
  }
  return str;
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function (data) {
  if (data.length === 0) return null;
  let ls = data.split(',');
  let root = new TreeNode(Number(ls[0]));
  let queue = [root];
  let i = 1;
  let current;
  while (queue.length > 0 && i < ls.length) {
    current = queue.shift();
    if (ls[i] !== 'n') {
      let left = new TreeNode(Number(ls[i]));
      current.left = left;
      queue.push(left);
    }
    i += 1;
    if (ls[i] !== 'n') {
      let right = new TreeNode(Number(ls[i]));
      current.right = right;
      queue.push(right);
    }
    i += 1;
  }
  return root;
};

// Time complexity is O(N)

// Space complexity is (N)
