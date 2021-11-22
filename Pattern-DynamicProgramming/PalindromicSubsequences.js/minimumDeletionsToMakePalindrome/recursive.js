const findMinimumDeletions = function (str) {
  let lps = recursive(str, 0, str.length - 1);
  return str.length - lps;
};

const recursive = function (str, start, end) {
  if (start > end) {
    return 0;
  }

  if (start === end) {
    return 1;
  }

  if (str[start] === str[end]) {
    return 2 + recursive(str, start + 1, end - 1);
  }

  let c1 = recursive(str, start + 1, end);
  let c2 = recursive(str, start, end - 1);

  return Math.max(c1, c2);
};

console.log(
  'Minimum number of deletions required ---> ' + findMinimumDeletions('abdbca')
);
console.log(
  'Minimum number of deletions required ---> ' + findMinimumDeletions('cddpd')
);
console.log(
  'Minimum number of deletions required ---> ' + findMinimumDeletions('pqr')
);
