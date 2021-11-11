let countRibbonPieces = function (ribbonLengths, total) {
  const n = ribbonLengths.length;

  // build grid
  const dp = Array(n)
    .fill(0)
    .map(() => Array(total + 1).fill(0));

  // fill first column
  for (let i = 0; i < n; i++) {
    dp[i][0] = 0;
  }

  //   fill grid with min values
  for (let i = 0; i < n; i++) {
    for (let j = 1; j <= total; j++) {
      dp[i][j] = Number.MIN_VALUE;
    }
  }

  for (let i = 0; i < n; i++) {
    for (let j = 1; j <= total; j++) {
      if (i > 0) {
        dp[i][j] = dp[i - 1][j];
      }
      if (
        ribbonLengths[i] <= j &&
        dp[i][j - ribbonLengths[i]] !== Number.MIN_VALUE
      ) {
        dp[i][j] = Math.max(dp[i][j], 1 + dp[i][j - ribbonLengths[i]]);
      }
    }
  }

  return dp[n - 1][total] === Number.MIN_VALUE ? -1 : dp[n - 1][total];
};

console.log(
  `Maximum number of ribbons: ---> ${countRibbonPieces([2, 3, 5], 5)}`
);
console.log(`Maximum number of ribbons: ---> ${countRibbonPieces([2, 3], 7)}`);
console.log(
  `Maximum number of ribbons: ---> ${countRibbonPieces([3, 5, 7], 13)}`
);
console.log(`Maximum number of ribbons: ---> ${countRibbonPieces([3, 5], 7)}`);
