let mappings = {
  0: 0,
  1: 1,
  2: 'abc',
  3: 'def',
  4: 'ghi',
  5: 'jkl',
  6: 'mno',
  7: 'pqrs',
  8: 'tuv',
  9: 'wxyz',
};

let letterCombinations = function (digits) {
  let result = [];
  if (digits.length === 0) return result;
  let mappings = {
    0: 0,
    1: 1,
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
  };
  dfs(digits, 0, mappings, result, '');
  return result;
};

let dfs = function (digits, currentIndex, mappings, result, path) {
  if (path.length === digits.length) {
    result.push(path);
    return;
  }

  let letters = mappings[digits[currentIndex]];
  for (let i of letters) {
    dfs(digits, currentIndex + 1, mappings, result, path + i);
  }
};
