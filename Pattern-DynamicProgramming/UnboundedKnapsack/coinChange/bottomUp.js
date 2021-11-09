let countChange = function (denominations, total) {
  if (denominations.length === 0 || total === 0) return 0;

  let n = denominations.length;
  let dp = Array(n)
    .fill(0)
    .map(() => Array(total + 1).fill(0));

  for (let i = 0; i < n; i++) {
    dp[i][0] = 1;
  }

  for (let i = 1; i <= total; i++) {
    if (denominations[0] <= i) {
      dp[0][i] = 1;
    }
  }

  for (let i = 1; i < n; i++) {
    for (let j = 1; j <= total; j++) {
      if (i > 0) {
        dp[i][j] = dp[i - 1][j];
      }
      if (denominations[i] <= j) {
        dp[i][j] += dp[i][j - denominations[i]];
      }
    }
  }

  return dp[n - 1][total];
};

console.log(`Number of ways to make change: ---> ${countChange([1, 2, 3], 5)}`);
