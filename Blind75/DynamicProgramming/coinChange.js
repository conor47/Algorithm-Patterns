// You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

// Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

// You may assume that you have an infinite number of each kind of coin.

// Example 1:

// Input: coins = [1,2,5], amount = 11
// Output: 3
// Explanation: 11 = 5 + 5 + 1

// Example 2:

// Input: coins = [2], amount = 3
// Output: -1

// Example 3:

// Input: coins = [1], amount = 0
// Output: 0

// Example 4:

// Input: coins = [1], amount = 1
// Output: 1

// Example 5:

// Input: coins = [1], amount = 2
// Output: 2

// Constraints:

//     1 <= coins.length <= 12
//     1 <= coins[i] <= 231 - 1
//     0 <= amount <= 104

var coinChange = function (denominations, total) {
  if (total === 0) return 0;

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

  for (let i = 0; i < n; i++) {
    for (let j = 0; j <= total; j++) {
      if (i > 0) {
        dp[i][j] = dp[i - 1][j];
      }

      if (denominations[i] <= j) {
        dp[i][j] = Math.min(dp[i][j], dp[i][j - denominations[i]] + 1);
      }
    }
  }

  return dp[n - 1][total] === Number.MAX_VALUE ? -1 : dp[n - 1][total];
};
