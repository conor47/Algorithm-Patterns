const findMinimumDeletions = function (str) {
  let lcs = helper(str);
  return str.length - lcs;
};

const helper = function (str) {
  const dp = Array(str.length)
    .fill(0)
    .map(() => Array(str.length).fill(0));

  for (let i = 0; i < str.length; i++) {
    dp[i][i] = 1;
  }

  for (let start = str.length - 1; start >= 0; start--) {
    for (let end = start + 1; end < str.length; end++) {
      if (str[start] === str[end]) {
        dp[start][end] = 2 + dp[start + 1][end - 1];
      } else {
        dp[start][end] = Math.max(dp[start + 1][end], dp[start][end - 1]);
      }
    }
  }

  return dp[0][str.length - 1];
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
