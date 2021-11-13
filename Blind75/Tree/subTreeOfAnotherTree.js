// Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

// A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

const isSubtree = function (root, subRoot) {
  if (root == null) {
    return false;
  }

  if (validate(root, subRoot)) {
    return true;
  }

  return validate(root.left, subRoot) || validate(root.right, subRoot);
};

const validate = function (r, s) {
  if (r == null || s == null) {
    return s == null && r == null;
  } else if (r.val == s.val) {
    return validate(r.left, s.left) && validate(r.right, s.right);
  } else {
    return false;
  }
};
