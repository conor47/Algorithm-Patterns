const canPartition = function (num, sum) {
  if (num.length === 0) return false;

  let n = num.length;

  //   build grid
  let dp = Array(n)
    .fill(false)
    .map(() => Array(sum + 1).fill(false));

  for (let i = 0; i < n; i++) {
    dp[i][0] = true;
  }

  for (let i = 1; i <= sum; i++) {
    dp[0][i] = num[0] === i;
  }

  for (let i = 1; i < n; i++) {
    for (let j = 1; j <= sum; j++) {
      if (dp[i - 1][j]) {
        dp[i][j] = dp[i - 1][j];
      } else if (num[i] <= j) {
        dp[i][j] = dp[i - 1][j - num[i]];
      }
    }
  }

  return dp[n - 1][sum];
};

console.log(`Can partitioning be done: ---> ${canPartition([1, 2, 3, 4], 6)}`);
console.log(
  `Can partitioning be done: ---> ${canPartition([1, 2, 7, 1, 5], 10)}`
);
console.log(`Can partitioning be done: ---> ${canPartition([1, 3, 4, 8], 6)}`);
console.log(`Can partitioning be done: ---> ${canPartition([1, 3, 4, 8], 16)}`);
