// Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C.’ Each item can only be selected once, which means either we put an item in the knapsack or we skip it.

function solveKnapsack(profits, weights, capacity) {
  const n = profits.length;

  //   sanity checks
  if (profits.length !== weights.length || capacity <= 0 || n === 0) return 0;

  //   build out grid
  const dp = Array(n)
    .fill(0)
    .map(() => Array(capacity + 1).fill(0));

  // fill first capacity 0 columns with 0
  for (let i = 0; i < n; i++) {
    dp[i][0] = 0;
  }

  //  if we only have one item then add it if it does not exceed the capacity

  for (let i = 0; i <= capacity.length; i++) {
    if (weights[0] <= c) dp[0][c] = profits[0];
  }

  //   process all subarrays for all capacities

  //   loop for rows
  for (let i = 1; i < n; i++) {
    //   loop for columns
    for (let j = 1; j <= capacity; j++) {
      let profit1 = 0;
      let profit2 = 0;

      //   weight of current item is within the capacity
      if (weights[i] <= j) {
        profit1 = profits[i] + dp[i - 1][j - weights[i]];
      }

      profit2 = dp[i - 1][j];

      dp[i][j] = Math.max(profit1, profit2);
    }
  }

  return dp[n - 1][capacity];
}

// This solution has a space and time complexity of O(n * c)

var profits = [1, 6, 10, 16];
var weights = [1, 2, 3, 5];
console.log(
  `Total knapsack profit: ---> ${solveKnapsack(profits, weights, 7)}`
);
console.log(
  `Total knapsack profit: ---> ${solveKnapsack(profits, weights, 6)}`
);
