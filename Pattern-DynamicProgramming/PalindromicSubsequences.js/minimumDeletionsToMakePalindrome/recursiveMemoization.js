const findMinimumDeletions = function (str) {
  const dp = [];
  let lps = recursive(str, 0, str.length - 1, dp);
  return str.length - lps;
};

const recursive = function (str, start, end, dp) {
  if (start > end) {
    return 0;
  }

  if (start === end) {
    return 1;
  }

  let key = `${start}-${end}`;

  if (typeof dp[key] === 'undefined') {
    if (str[start] === str[end]) {
      return 2 + recursive(str, start + 1, end - 1, dp);
    }

    let c1 = recursive(str, start + 1, end, dp);
    let c2 = recursive(str, start, end - 1, dp);

    dp[key] = Math.max(c1, c2);
  }
  return dp[key];
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
