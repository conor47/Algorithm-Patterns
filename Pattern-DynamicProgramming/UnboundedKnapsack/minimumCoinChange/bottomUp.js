let countChange = function (denominations, total) {
  if (total === 0 || denominations.length === 0) return 0;

  const n = denominations.length;

  const dp = Array(n)
    .fill(0)
    .map(() => Array(total + 1).fill(0));

  for (let i = 0; i < n; i++) {
    dp[i][0] = 0;
  }

  for (let i = 0; i < n; i++) {
    for (let j = 1; j <= total; j++) {
      dp[i][j] = Number.MAX_VALUE;
    }
  }

  for (let i = 1; i < n; i++) {
    for (let j = 1; j <= total; j++) {
      dp[i][j] = dp[i - 1][j];

      if (denominations[i] <= j) {
        dp[i][j] = Math.min(dp[i][j], dp[i][j - denominations[i]] + 1);
      }
    }
  }

  return dp[n - 1][total] === Number.MAX_VALUE ? -1 : dp[n - 1][total];
};

// Time and space complexity of O(N * C) where N is the number of coin denominations and C is the total

console.log(`Number of ways to make change: ---> ${countChange([1, 2, 3], 5)}`);
console.log(
  `Number of ways to make change: ---> ${countChange([1, 2, 3], 11)}`
);
console.log(`Number of ways to make change: ---> ${countChange([1, 2, 3], 7)}`);
console.log(`Number of ways to make change: ---> ${countChange([3, 5], 7)}`);
