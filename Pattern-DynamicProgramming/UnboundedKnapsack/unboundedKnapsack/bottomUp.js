let solveKnapsack = function (profits, weights, capacity) {
  if (
    profits.length === 0 ||
    profits.length !== weights.length ||
    capacity <= 0
  )
    return 0;

  let n = profits.length;

  //   build the grid
  let dp = Array(n)
    .fill(0)
    .map(() => Array(capacity + 1).fill(0));

  // fill first column

  for (let i = 0; i < n; i++) {
    dp[i][0] = 0;
  }

  //  fill first row

  for (let i = 1; i <= capacity; i++) {
    if (weights[0] <= i) {
      dp[0][i] = profits[0];
    }
  }

  for (let i = 1; i < n; i++) {
    for (j = 1; j <= capacity; j++) {
      let profit1 = 0;
      let profit2 = 0;
      if (weights[i] <= j) {
        profit1 += profits[i] + dp[i - 1][j - weights[i]];
      }
      profit2 = dp[i - 1][j];
      dp[i][j] = Math.max(profit1, profit2);
    }
  }

  return dp[n - 1][capacity];
};

// Time complexity is O(N * C)

// Space complexity is O(N * C)

var profits = [15, 50, 60, 90];
var weights = [1, 3, 4, 5];
console.log(
  `Total knapsack profit: ---> ${solveKnapsack(profits, weights, 8)}`
);
console.log(
  `Total knapsack profit: ---> ${solveKnapsack(profits, weights, 6)}`
);
