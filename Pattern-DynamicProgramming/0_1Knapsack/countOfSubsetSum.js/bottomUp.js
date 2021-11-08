const countSubsets = function (num, sum) {
  let n = num.length;

  //   build the grid
  let dp = Array(n)
    .fill(0)
    .map(() => Array(sum + 1).fill(0));

  // fill the first column

  for (let i = 0; i < n; i++) [(dp[i][0] = 1)];

  // fill the first row
  for (let i = 1; i <= sum; i++) {
    dp[0][i] = num[0] === i;
  }

  for (let i = 1; i < n; i++) {
    for (let j = 1; j <= sum; j++) {
      //   exclude the number
      dp[i][j] = dp[i - 1][j];

      // include the number if it does not exceed the sum
      if (num[i] <= j) {
        dp[i][j] += dp[i - 1][j - num[i]];
      }
    }
  }

  return dp[n - 1][sum];
};

console.log(`Count of subset sum is: ---> ${countSubsets([1, 1, 2, 3], 4)}`);
console.log(`Count of subset sum is: ---> ${countSubsets([1, 2, 7, 1, 5], 9)}`);
