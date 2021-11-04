// Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

const generateParenthesis = (n) => {
  const result = [];

  const backtrack = (left, right, str) => {
    //   if we ever have more open parenthesis than closing left then we return. Invalid case
    if (left > right) return;

    // if we reach this point given our constraints then we know we have generated a valid string
    if (left === 0 && right === 0) {
      result.push(str);
      return;
    }

    if (left > 0) {
      backtrack(left - 1, right, str + '(');
    }
    if (r > 0) {
      backtrack(left, right - 1, str + ')');
    }
  };
  backtrack(n, n, '');
  return result;
};

// Space complexity of this solution is the max size of the call stack during execution which is
